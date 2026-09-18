from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests


@tool
def multiply(a:int, b:int) -> int:
    """Multiplies two numbers."""
    return a * b

result = multiply.invoke({'a':4, 'b':5})
print(f"Result of multiplication: {result}")


# Tool Binding
llm = ChatOpenAI()
llm_with_tools = llm.bind_tools([multiply])

print(llm_with_tools.invoke("Hi How are you?"))

print("\n")

print(llm_with_tools.invoke("Multiply 4 and 5"))


print("\n")
result = llm_with_tools.invoke("Multiply 4 and 5").tool_calls[0]
print(f"Result of tool call: {result}")

out = multiply.invoke(result["args"])
print(f"Final result: {out}")

# Whole 
print("\n")
out = multiply.invoke(result)
print("Tool Message:", out)





query = HumanMessage(content="Multiply 3 and 5")
message = [query]

result = llm_with_tools.invoke(message)

message.append(result)

tool_result = multiply.invoke(result.tool_calls[0])
message.append(tool_result)
print("\n \n")
print(message)


print("\n \n \n")
final= llm_with_tools.invoke(message)
print(final)