from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_splitter = SemanticChunker(
    embeddings=OpenAIEmbeddings(),  # Changed 'embedding' -> 'embeddings'
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1.0
)

text = """
LangChain is a framework for developing applications powered by language models. 
It enables applications that are context-aware and reason based on provided material.

Apples, bananas, and oranges are common fruits. 
They contain various vitamins and minerals beneficial for human health.
"""

docs = text_splitter.split_text(text)
print(docs)
print(f"Number of chunks: {len(docs)}")

#test zshrc