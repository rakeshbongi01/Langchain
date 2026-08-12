from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv, parser
from langchain.schema.runnable import RunnableSequence

load_dotenv()

prompt= PromptTemplate(
    template="Write a Joke about {topic}.",
    input_variables=["topic"]
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = RunnableSequence(prompt, model, parser)

print(chain.invoke({"topic": "programming"}))


prompt2= PromptTemplate(
    template="Explain about the {text}.",
    input_variables=["text"]
)

chain = RunnableSequence(prompt, model, parser,prompt2, model, parser)

print(chain.invoke({"topic": "programming"}))