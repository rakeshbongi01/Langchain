from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class MultiplyInput(BaseModel):
    a: int = Field(..., description="First number")
    b: int = Field(..., description="Second number")


class MultiplyTool(BaseTool):
    name: str = "multiply"
    description: str = "Multiplies two numbers together."
    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a: int, b: int) -> int:
        return a * b

multiply_tool = MultiplyTool()
print(multiply_tool.invoke({"a": 5, "b": 3}))  # Example usage