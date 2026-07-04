from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful {domain} assistant."),   
    ("human", "Explain in simple terms how {concept} works."),
]
)

prompt = chat_template.invoke({"domain": "math", "concept": "calculus"})
print(prompt)

prompt = chat_template.format(domain="science", concept="gravity")
print(prompt)