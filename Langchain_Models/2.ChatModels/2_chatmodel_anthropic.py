from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-3.5", max_completion_tokens=10)
response = model.invoke("What is the capital of France?")
print(response)
print(response.content)