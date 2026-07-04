from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=40)
result = embeddings.embed_query("What is the capital of France?")
print(result)
print(len(result))
print(type(result))
print(str(result))