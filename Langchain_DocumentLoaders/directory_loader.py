from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="/Users/rakesh/Documents/Learning/Langchain/Langchain_DocumentLoaders/books/",
    glob="*.pdf",
    loader_cls=PyPDFLoader)

docs = loader.load()

print(len(docs))
print(docs[0].metadata)

print(docs[4].page_content)

# All At Once Loading
docs = loader.load()

for doc in docs:
    print(doc.metadata)
    print(doc.page_content)



# One By One Loading
docs = loader.lazy_load()

for doc in docs:
    print(doc.metadata)
    print(doc.page_content)