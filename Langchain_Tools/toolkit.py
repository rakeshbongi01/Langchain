from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers together."""
    return a * b

@tool
def add(a: int, b: int) -> int:
    """Adds two numbers together."""
    return a + b

class MatchToolkit:
    def get_tools(self):
        return [multiply, add]

toolkit = MatchToolkit()
tools = toolkit.get_tools()

for tool in tools:
    print(f"Tool name: {tool.name}, Description: {tool.description}")