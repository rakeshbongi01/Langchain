from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

result = search.run("What is the capital of France?")

print(result)


print(search.name)
print(search.description)
print(search.args)