from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()

# 1st prompt -> Detailed Report
template1= PromptTemplate(
    template=' Write a detailed report on the topic: {topic}.',
    input_variables=['topic']
)

# 2nd prompt -> Extracting the summary from the detailed report
template2 = PromptTemplate(
    template='write 5 lines of summary on following text.\n {text}',
    input_variables=['text']
)


# prompt1= template1.invoke({'topic': 'Black Hole'})
# result1 = model.invoke(prompt1)

# prompt2= template2.invoke({'text': result1.content})
# result2 = model.invoke(prompt2)

# print('Detailed Report: \n', result1.content)
# print('Summary: \n', result2.content)


parser= StrOutputParser()

chain  = template1 | model | parser| template2 | model | parser

result = chain.invoke({'topic': 'Black Hole'})
print('Summary: \n', result)