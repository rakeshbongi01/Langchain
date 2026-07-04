from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
import streamlit as st

load_dotenv()

model = ChatOpenAI(model="gpt-4", max_completion_tokens=2500)

st.header("Research Paper Explanation Generator")

paper_input = st.selectbox("Select Research Paper Name", ["Attention Is All You Need",
"BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-ShotLearners", "Diffusion Models Beat GANs on Image Synthesis"] )
style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-", "Technical","Code-Oriented", "Mathematical"] )
length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5paragraphs)", "Long (detailed explanation)"] )


prompt_template = load_prompt("template.json")
# Placeholder for the generated explanation
prompt = prompt_template.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input
})


if st.button("Generate Explanation"):
    result = model.invoke(prompt)
    st.write(result.content)




# streamlit run /Users/rakesh/Documents/Learning/Langchain/Langchain_Prompts/3_prompts_ui.py