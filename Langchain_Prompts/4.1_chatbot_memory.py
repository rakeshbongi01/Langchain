from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4", max_completion_tokens=2500)

chat_list = []

while True:
    user_input = input("You: ")
    chat_list.append(user_input)
    if user_input == "exit":
        print("Chatbot: Goodbye!")
        break
    response = model.invoke(chat_list)
    chat_list.append( response.content)
    print(f"Chatbot: {response.content}")
print("Chat history:", chat_list)