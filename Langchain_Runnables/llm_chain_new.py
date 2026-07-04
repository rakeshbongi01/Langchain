from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Load environment variables from .env file
load_dotenv()

# 1. Use ChatOpenAI for chat models like gpt-3.5-turbo or gpt-4o
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# 2. Use ChatPromptTemplate for modern chains
prompt_template = ChatPromptTemplate.from_template(
    "Write a short story about {topic}."
)

# 3. Create a chain using the modern pipe (|) operator (LCEL)
# This replaces the deprecated LLMChain
chain = prompt_template | llm

# 4. Run the chain using .invoke() instead of the deprecated .run()
topic = "a brave knight"
response = chain.invoke({"topic": topic})

# The response from a ChatModel is a message object; extract the text content
print(response.content)