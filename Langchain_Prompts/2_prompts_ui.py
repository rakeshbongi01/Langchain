from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import streamlit as st

load_dotenv()

model = ChatOpenAI(model="gpt-4", max_completion_tokens=2500)

st.header("Research Paper Explanation Generator")

paper_input = st.selectbox("Select Research Paper Name", ["Attention Is All You Need",
"BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-ShotLearners", "Diffusion Models Beat GANs on Image Synthesis"] )
style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-", "Technical","Code-Oriented", "Mathematical"] )
length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5paragraphs)", "Long (detailed explanation)"] )



# Define the prompt template
prompt_template = PromptTemplate(
    # Validate that the template is correctly formatted and contains the required input variables
    validate_template=True,
    input_variables=['paper_input', 'style_input', 'length_input'],
    template="""Please summarize the research paper titled {paper_input} with the following specifications:
                Explanation Style: {style_input}
                Explanation Length: {length_input}
                1. Mathematical Details:
                - Include relevant mathematical equations if present in the paper.
                - Explain the mathematical concepts using simple, intuitive code snippets where applicable.
                2. Analogies:
                - Use relatable analogies to simplify complex ideas.
                If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.
                Ensure the summary is clear, accurate, and aligned with the provided style and length.
    """
)

# Placeholder for the generated explanation
prompt = prompt_template.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input
})


if st.button("Generate Explanation"):
    result = model.invoke(prompt)
    st.write(result.content)




# streamlit run /Users/rakesh/Documents/Learning/Langchain/Langchain_Prompts/2_prompts_ui.py