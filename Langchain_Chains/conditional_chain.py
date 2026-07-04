from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal
load_dotenv()

model  = ChatOpenAI()

parser = StrOutputParser()

class Feedback(BaseModel):
    category: Literal['positive', 'negative'] = Field(description="The category of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1= PromptTemplate(
    template=" Classify the following text into one of the categories: 'positive', 'negative' Text: {feedback} \n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser2.get_format_instructions()}
)

prompt2= PromptTemplate(
    template=" Write  an appropriate response to the following positive feedback: {feedback} \n",
    input_variables=["feedback"]
)

prompt3= PromptTemplate(
    template=" Write  an appropriate response to the following negative feedback: {feedback} \n",
    input_variables=["feedback"]
)

classifier_chain = prompt1 | model | parser2

#result = classifier_chain.invoke({"feedback": "I love this product! It works great and exceeds my expectations."})
#print(result)

branch_chain = RunnableBranch(
    (lambda x:x.category == 'positive', prompt2 | model | parser),
    (lambda x:x.category == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "Sorry, I couldn't classify the feedback.")

)

response_chain = classifier_chain | branch_chain
result = response_chain.invoke({"feedback": "I love this product! It works great and exceeds my expectations."})
print(result)
response_chain.get_graph().print_ascii()
