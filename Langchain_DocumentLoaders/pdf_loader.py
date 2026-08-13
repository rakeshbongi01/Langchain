from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv



loader= PyPDFLoader("/Users/rakesh/Documents/Learning/Langchain/Langchain_DocumentLoaders/cheat_sheet_github.pdf")

docs= loader.load()

print(docs)
print(len(docs))

print("\n")

print(docs[0].page_content)
