from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text = """
# Clone the repository and install dependencies
git clone [https://github.com/example/sample-project.git](https://github.com/example/sample-project.git)
cd sample-project
pip install -r requirements.txt

# Run test suite
pytest tests/ -v
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=100,
    chunk_overlap=0
)

chunks = splitter.split_text(text)
print("Number of chunks:", len(chunks))
print("Chunks:", chunks)