from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv, parser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough,RunnableLambda


load_dotenv()

def word_counter(text: str) -> int:
    """Counts the number of words in a given text."""
    return len(text.split())

runnable_word_counter = RunnableLambda(word_counter)

print(runnable_word_counter.invoke("This is a sample text to count the number of words."))


prompt1= PromptTemplate(
    template="Generate Joke about {topic}.",
    input_variables=["topic"]
)

model = ChatOpenAI()

parser = StrOutputParser()

joke_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    #'word_count': runnable_word_counter
    'word_count': RunnableLambda(lambda text: len(text.split()))
})

final_chain = RunnableSequence(joke_chain, parallel_chain)


print(final_chain.invoke({"topic": "AI in healthcare"}))