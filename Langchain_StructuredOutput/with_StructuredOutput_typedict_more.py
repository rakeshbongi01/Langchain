from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional,Literal

load_dotenv()

model=ChatOpenAI()

class Review(TypedDict):
    key_themes: Annotated[list[str], "The All themes discussed in the review"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["pos", "neg"], "The sentiment of the review"]
    pros: Optional[Annotated[list[str], "The positive aspects mentioned in the review"]]
    cons: Optional[Annotated[list[str], "The negative aspects mentioned in the review"]]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""TThe hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. 
Hoping for a software update to fix this.

I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3
ning fast-whether 2'm ga
processor makes everything lightning fast-whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.
The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.
However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with bloatware-why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.
Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging S-Pen support is unique and useful
Cons:
Bulky and heavy-not great for one-handed use
Bloatware still exists in One UI
Expensive compared to competitors""")

print(result)
#print(result['summary'])
print(result['sentiment'])
#print(type(result))


# a prompt will be generated to extract the summary and sentiment from the review, and the output will be a dictionary with the keys 'summary' and 'sentiment'.
#  The values will be the extracted summary and sentiment from the review.


# Will work without annotaded but by using Annotated, we can provide additional information about the type, such as a description or constraints. 
# This can be useful for documentation purposes or for tools that can utilize this metadata. In this case, we are simply defining the structure of the output without any additional metadata, so it is not strictly necessary to use Annotated.