from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", max_completion_tokens=10)
response = model.invoke("What is the capital of France?")
print(response)

