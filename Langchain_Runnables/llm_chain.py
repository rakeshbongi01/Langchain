""" 
This won't work  because it's using an outdated syntax that doesn't play well with newer versions of LangChain and the OpenAI library (version 1.0.0+).

Specifically, you are trying to pass a Chat Model (gpt-3.5-turbo) into a legacy completion class (OpenAI), while using the deprecated LLMChain and .run() syntax.

To fix this, you should upgrade to LCEL (LangChain Expression Language), which is the modern standard for building chains.
"""

from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# load th llm
llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

# create a prompt template
prompt_template = PromptTemplate(
    input_variables=["topic"],
    template="Write a short story about {topic}."
)

# create an LLMChain
llm_chain = LLMChain(llm=llm, prompt=prompt_template)

# run the chain with a specific topic
topic = "a brave knight"
story = llm_chain.run(topic=topic)
print(story)
