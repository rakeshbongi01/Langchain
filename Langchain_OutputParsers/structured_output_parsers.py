from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatOpenAI()
response_schemas = [
    ResponseSchema(name="fact_1", description="A fact1 about topic."),
    ResponseSchema(name="fact_2", description="A fact2 about topic."),
    ResponseSchema(name="fact_3", description="A fact3 about topic."),
]
parser = StructuredOutputParser.from_response_schemas(response_schemas)

template= PromptTemplate(
    template="give me 3 facts about {topic} \n {format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain= template | model | parser
result = chain.invoke({"topic": "black hole"})
print('Chain Parsed Result: \n', result)

# OR
prompt = template.invoke({"topic": "black hole"})
result = model.invoke(prompt)
print('Result: \n', result)
# we need to send result.content to parser as it is a ChatMessage object and we need to extract the content from it before parsing
parsed_result = parser.parse(result.content)
print('Parsed Result: \n', parsed_result)