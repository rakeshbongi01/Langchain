from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

schema = {
    "title": "student_analysis",
    "description": "Analyze a student and return structured data",
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "summary": {"type": "string"},
        "sentiment": {"type": "string"}
    },
    "required": ["name", "age", "summary", "sentiment"]
}

structured_model = model.with_structured_output(schema)

prompt = "Anjali Sharma is a 19 year old student who is hardworking and focused."

result = structured_model.invoke(prompt)

print(result)
print(result["summary"])
print(result["sentiment"])
print(type(result))