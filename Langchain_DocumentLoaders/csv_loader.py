from langchain_community.document_loaders import CSVLoader

file_path = "path/to/your/file.csv"  # Replace with the actual path to your CSV file
loader = CSVLoader(file_path)
docs = loader.load()