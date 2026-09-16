from langchain_core.tools import tool

#step 1
def multiply(a,b):
    return a * b

#step 2
def mulyiply(a:int, b:int) -> int:
    return a * b

#step 3
"""Transforms the function into a BaseTool object. You can now pass this directly to an agent or a model using .bind_tools(), and the LLM will know how to call it autonomously."""
"""It Became Runnable"""
@tool
def multiply(a:int, b:int) -> int:
    """Multiplies two numbers together."""
    return a * b

result = multiply.invoke({"a": 3, "b": 4})
print(result)

print(multiply.name)
print(multiply.description)
print(multiply.args)

# LLM will see this
print(multiply.args_schema.model_json_schema())