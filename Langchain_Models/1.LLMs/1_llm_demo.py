from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")

response = llm("What are three capitals of Andhra Pradesh?")
print(response)