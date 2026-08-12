from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv, parser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough,RunnableLambda, RunnableBranch


load_dotenv()

prompt1= PromptTemplate(
    template="Generate Detailed report about {topic}.",
    input_variables=["topic"]
)

prompt2= PromptTemplate(
    template="Summarise follwoing {text}.",
    input_variables=["text"]
)


model = ChatOpenAI()

parser = StrOutputParser()


report_generator_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 100, RunnableSequence(prompt2, model, parser)), 
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_generator_chain, branch_chain)

print(final_chain.invoke({"topic": "AI in healthcare"}))