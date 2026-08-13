from langchain_community.document_loaders import WebBaseLoader

url = "https://www.geeksforgeeks.org/dsa/must-do-coding-questions-for-product-based-companies/" 
loader = WebBaseLoader(url)
docs = loader.load()

print(len(docs))
print(docs[0].metadata)