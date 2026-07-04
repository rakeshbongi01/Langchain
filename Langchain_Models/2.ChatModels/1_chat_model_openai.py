from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4", max_completion_tokens=10)
response = model.invoke("What is the capital of France?")
print(response)
print(response.content)

""" Roughly tokesn are equal to words, so the above code will return a response with a maximum of 10 words. """


# model = ChatOpenAI(model="gpt-4", temperature=2, max_completion_tokens=10)
# response = model.invoke("Wrote a poem on the topic of 'The beauty of nature'.")
# print(response)
# print(response.content)