from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
import requests
from langchain_community.tools import DuckDuckGoSearchRun

@tool
def custom_duckduckgo_search(query: str) -> str:
    """
    A custom tool that uses DuckDuckGo's search engine to fetch search results.
    """
    search_tool = DuckDuckGoSearchRun()
    return search_tool.invoke(query)

#results = search_tool.invoke("Top News in India Today")
llm = ChatOpenAI()




from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

prompt = hub.pull("hwchase17/react")


agent = create_react_agent(
    llm = llm,
    tools = [custom_duckduckgo_search],
    prompt = prompt
)

agent_executor = AgentExecutor(
    agent = agent,
    tools = [custom_duckduckgo_search],
    verbose = True
)

response = agent_executor.invoke(
    {"input": "3 Ways to reach Goa from Hyderabad?"}
)
print(response)