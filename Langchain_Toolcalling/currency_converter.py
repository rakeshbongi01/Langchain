from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
import os
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool, InjectedToolArg
from langchain_core.messages import HumanMessage, ToolMessage
import requests
from typing import Annotated
import json

@tool
def currency_conversion_rate(base_currency: str, target_currency: str) -> dict:
    """
    This function converts an amount from a base currency to a target currency using the ExchangeRate-API.
    """
    api_key = os.getenv("EXCHANGE_RATE_API_KEY")
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}"

    response = requests.get(url)
    return response.json()

@tool
def convert_currency(base_amount: float, conversion_rate: Annotated[float, InjectedToolArg]) -> float:
    """
    This function converts an amount from a base currency to a target currency using the provided conversion rate.
    """
    return base_amount * conversion_rate

# Tool Binding
llm = ChatOpenAI()
llm_with_tool = llm.bind_tools([currency_conversion_rate, convert_currency])

messages = [HumanMessage("What is the conversion rate from USD to INR? Based on that, convert 100 USD to INR.")]

# --- Step 1: First invocation (Gets currency conversion rate) ---
ai_message = llm_with_tool.invoke(messages)
messages.append(ai_message) # Always append the AI message containing tool calls to history

conversion_rate = None

for tool_call in ai_message.tool_calls:
    print("Executing:", tool_call['name'])
    if tool_call["name"] == "currency_conversion_rate":
        # Invoke the tool
        result = currency_conversion_rate.invoke(tool_call["args"])
        conversion_rate = result.get("conversion_rate")
        print(f"Conversion Rate from USD to INR: {conversion_rate}")
        
        # Append ToolMessage back to messages
        messages.append(ToolMessage(content=json.dumps(result), tool_call_id=tool_call["id"]))

# --- Step 2: Second invocation (Passes history back so LLM calls convert_currency) ---
# Since the LLM now has the conversion rate result in history, it can generate the next tool call.
ai_message_2 = llm_with_tool.invoke(messages)
messages.append(ai_message_2)

for tool_call in ai_message_2.tool_calls:
    print("Executing:", tool_call['name'])
    if tool_call["name"] == "convert_currency":
        # Inject the runtime conversion_rate we saved earlier
        tool_call["args"]["conversion_rate"] = conversion_rate
        
        result = convert_currency.invoke(tool_call["args"])
        print(f"Converted Amount: {result}")
        
        messages.append(ToolMessage(content=json.dumps({"converted_amount": result}), tool_call_id=tool_call["id"]))

# Final response from LLM summarizing everything
final_response = llm_with_tool.invoke(messages)
print("\nFinal AI Response:")
print(final_response.content)