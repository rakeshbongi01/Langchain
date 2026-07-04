from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()

model = ChatOpenAI(model="gpt-4")

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the Pay of agentic ai engineer in india with 7 years backend and data engineering experience and learned agentic ai engineering skills IIIT Hyderabad.") 
]


result = model(messages)

messages.append(AIMessage(content=result.content))

print(messages)




# We can use this in our 4.1_chatbot_memory.py