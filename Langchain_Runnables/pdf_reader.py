import os
from dotenv import load_dotenv
# Corrected and updated imports
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI

# Load environment variables from .env file (Move this to the top before invoking clients)
load_dotenv()

# 1. Load the PDF document properly
loader = PyPDFLoader("Langchain_Runnables/Kotak_report_June23.pdf")
documents = loader.load()

# 2. Split the document into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(documents)

# 3. Create embeddings for the document chunks and store them in a FAISS vector store
vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())

# 4. Create a retriever from the vector store
retriever = vectorstore.as_retriever()

# 5. Manually retrieve relevant documents using the retriever
query = "which is highest revenue generating segment/sector in Kotak report?"
retrieved_docs = retriever.get_relevant_documents(query)

# Combine the retrieved documents into a single string
combined_docs = " ".join([doc.page_content for doc in retrieved_docs])

# 6. Initialize the LLM
llm = ChatOpenAI()

# Manually pass retrieved text to the LLM for processing
prompt = f"Answer the following question based on the provided text: {query}\n\nText: {combined_docs}"

# Modern LangChain uses .invoke() instead of calling the object directly
response = llm.invoke(prompt)
print(response.content)
