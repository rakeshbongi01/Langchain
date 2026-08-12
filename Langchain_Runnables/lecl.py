from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
# 1. Define components
prompt = ChatPromptTemplate.from_template("Summarize the following topic in two sentences: {topic}")
model = ChatOpenAI(model="gpt-4o")
parser = StrOutputParser()

# 2. Chain components using LCEL pipe operator (|)
chain = prompt | model | parser

# 3. Invoke the chain
response = chain.invoke({"topic": "Apache Airflow"})
print(response)