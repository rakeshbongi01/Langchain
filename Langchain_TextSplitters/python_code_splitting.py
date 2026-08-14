from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text = """
def my_function():
    # This is a sample function
    a = 10
    b = 20
    return a + b
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=50,
    chunk_overlap=0
)


chunks = splitter.split_text(text)

print("Number of chunks:", len(chunks))
print("Chunks:", chunks)