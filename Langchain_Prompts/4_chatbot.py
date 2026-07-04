from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4", max_completion_tokens=2500)

while True:
    user_input = input("You: ")

    if user_input == "exit":
        print("Chatbot: Goodbye!")
        break
    response = model.invoke(user_input)
    print(f"Chatbot: {response.content}")