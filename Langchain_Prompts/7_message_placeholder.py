from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# Chat template
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful customer support agent."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}"),
])


chat_history = []
# load history
with open("/Users/rakesh/Documents/Learning/Langchain/Langchain_Prompts/7_chat_history.txt", "r") as f:
    chat_history.extend(f.readlines())

print(chat_history)

# create prompt
prompt = chat_template.invoke({"chat_history": chat_history, "query": "What is the status of my refund?"})

print(prompt)