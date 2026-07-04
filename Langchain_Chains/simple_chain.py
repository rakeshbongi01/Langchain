from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


prompt = PromptTemplate(
    template="generate 5 facts about {topic}",
    input_variables=["topic"]
)

model = ChatOpenAI()

parser = StrOutputParser()

# Langchain expression language to create a chain
chain = prompt | model | parser

print('/n Chain Steps:/n')
chain.get_graph().print_ascii()
result = chain.invoke({"topic": "space"})
print(result)