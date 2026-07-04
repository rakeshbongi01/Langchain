from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

# Initialize the OpenAI embeddings model
embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=300)

documents=[
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "Who is the Rohit Sharma?"
 
documents_embeddings = embeddings_model.embed_documents(documents)
query_embedding = embeddings_model.embed_query(query)

similarities = cosine_similarity([query_embedding], documents_embeddings)[0]

index, score = sorted(list(enumerate(similarities)), key=lambda x: x[1], reverse=True)[0]
print(f"Most similar document: '{documents[index]}' with similarity score: {score:.4f}")
