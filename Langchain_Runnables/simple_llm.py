from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

# Initialize the LLM
llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

# Define a prompt template
prompt_template = PromptTemplate(
    input_variables=["topic"],
    template="Write a short paragraph about {topic}."
)

# Define input
topic = input("Enter a topic: ")

# format the prompt manually using PromptTemplate
formatted_prompt = prompt_template.format(topic=topic)

# call the llm directly
response = llm.predict(formatted_prompt)

# Print the response
print("Response from LLM:", response)