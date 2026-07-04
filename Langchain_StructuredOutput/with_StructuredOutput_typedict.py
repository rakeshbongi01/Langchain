from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

model=ChatOpenAI()

class Review(TypedDict):
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "The sentiment of the review (positive/negative/neutral)"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. 
             Hoping for a software update to fix this.""")

print(result)
print(result['summary'])
print(result['sentiment'])
print(type(result))


# a prompt will be generated to extract the summary and sentiment from the review, and the output will be a dictionary with the keys 'summary' and 'sentiment'.
#  The values will be the extracted summary and sentiment from the review.


# Will work without annotaded but by using Annotated, we can provide additional information about the type, such as a description or constraints. 
# This can be useful for documentation purposes or for tools that can utilize this metadata. In this case, we are simply defining the structure of the output without any additional metadata, so it is not strictly necessary to use Annotated.