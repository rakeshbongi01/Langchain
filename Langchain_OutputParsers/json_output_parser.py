from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatOpenAI()

parser= JsonOutputParser()

template1= PromptTemplate(
    template=' Write a detailed report on the black hole \n {format_instructions}.',
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# prompt = template1.format()
# result = model.invoke(prompt)
# print('Result: \n', result)
# parsed_result = parser.parse(result.content)
# print('Parsed Result: \n', parsed_result)


# or
print('\n Using Chain:\n')
chain = template1 | model | parser
# input variables are empty as we have partial variables in the template, so we can pass empty dict
result = chain.invoke({})
print('Chain Parsed Result: \n', result)