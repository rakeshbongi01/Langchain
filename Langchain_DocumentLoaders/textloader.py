from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

loader = TextLoader("/Users/rakesh/Documents/Learning/Langchain/Langchain_DocumentLoaders/AI_in_Agriculture.txt")

docs = loader.load()

print(type(docs))

print(len(docs))

print(docs[0])
print(type(docs[0]))

print(docs[0].page_content)
print(docs[0].metadata)

model = ChatOpenAI()

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Write a Summary about the following text: {text}",
    input_variables=["text"]
)

chain = prompt | model | parser

print(chain.invoke({"text": docs[0].page_content}))