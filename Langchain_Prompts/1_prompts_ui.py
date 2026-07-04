from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatOpenAI(model="gpt-4", max_completion_tokens=1000)

st.title("Langchain Prompts UI")
st.header("Enter your prompt below:")
user_input = st.text_input("Enter your prompt here:")

if st.button("Summarize"):
    result = model.invoke(user_input)
    st.write(result.content)



# to run
# streamlit run 1_prompts_ui.py
#streamlit run /Users/rakesh/Documents/Learning/Langchain/Langchain_Prompts/1_prompts_ui.py [ARGUMENTS]


""" Static vs Dynamic Prompts
Static prompts are pre-defined and do not change based on user input or context. They are fixed and can be used for specific tasks or scenarios. For example, 
a static prompt could be "What is the capital of France?" which will always yield the same response."

Dynamic prompts, on the other hand, are generated or modified based on user input, context, or other factors. They can adapt to different situations 
and provide more personalized responses. For example, a dynamic prompt could be "What is the capital of [country]?" where [country] is replaced with 
user input, allowing for a more flexible and interactive experience."

"""