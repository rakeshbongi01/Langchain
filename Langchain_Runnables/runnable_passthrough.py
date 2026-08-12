from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv, parser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

passthrough = RunnablePassthrough()

print(passthrough.invoke({"topic": "AI in healthcare"}))

prompt1= PromptTemplate(
    template="Generate Joke about {topic}.",
    input_variables=["topic"]
)

prompt2= PromptTemplate(
    template="Expalin the following Joke {text}.",
    input_variables=["text"]
)

model = ChatOpenAI()

parser = StrOutputParser()

joke_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_chain, parallel_chain)

print(final_chain.invoke({"topic": "AI in healthcare"}))

