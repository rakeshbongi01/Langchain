from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv, parser
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()

prompt1= PromptTemplate(
    template="Generate Tweet about {topic}.",
    input_variables=["topic"]
)

prompt2= PromptTemplate(
    template="Generate LinkedIn post about {topic}.",
    input_variables=["topic"]
)

model = ChatOpenAI()

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser)
}
)

results = parallel_chain.invoke({"topic": "AI in healthcare"})

print("Tweet:", results['tweet'])
print("LinkedIn Post:", results['linkedin'])