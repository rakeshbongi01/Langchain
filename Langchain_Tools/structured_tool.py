from langchain.tools import StructuredTool
from pydantic import BaseModel, Field

class MultiplyArgs(BaseModel):
    a: int = Field(required=True, description="The first number to multiply."),
    b: int = Field(required=True, description="The second number to multiply.")

def multiply(a: int, b: int) -> int:
    """Multiplies two numbers together."""
    return a * b

multiply_tool = StructuredTool(
    name="multiply",
    description="Multiplies two numbers together.",
    args_schema=MultiplyArgs,
    func=multiply
)

result = multiply_tool.invoke({"a": 3, "b": 4})
print(result)