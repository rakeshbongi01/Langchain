from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

import os

os.environ["HF_HOME"] = "D://blabla"

llm=HuggingFacePipeline.from_model_id(
    model_id="wangsheng/DeepSeekV4Chat",
    task="text-generation",
    pipeline_kwargs={"max_length": 2048}
)

model = chatHuggingFace(llm=llm)
result = model.invoke("What is the capital of France?")
print(result)