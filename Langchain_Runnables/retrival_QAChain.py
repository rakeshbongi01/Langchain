from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load environment variables from .env file (Move this to the top before invoking clients)
load_dotenv()

loader = PyPDFLoader("Langchain_Runnables/Kotak_report_June23.pdf")
documents = loader.load()

# Split the document into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(documents)

# Convert embeddings for the document chunks and store them in a FAISS vector store
vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())

# Create a retriever from the vector store
retriever = vectorstore.as_retriever()

llm = ChatOpenAI()

# Create a RetrievalQA chain using the LLM and the retriever
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)


# Ask a question and get an answer using the RetrievalQA chain
query = "which is highest revenue generating company in Kotak report?"
result = qa_chain({"query": query})
print("Answer:", result['result'])