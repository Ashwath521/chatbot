import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI model
llm = ChatOpenAI(model="gpt-4o")

# Define Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert AI Engineer. Provide answers based on the questions. Keep the response within 300 letters."),
    ("user", "{input}")
])

# Define LangChain pipeline
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Streamlit UI
st.title("🤖 GenAI Chatbot with LangChain & OpenAI")
st.write("Ask me anything about AI, LangChain, or Generative AI!")

# User input
user_input = st.text_input("Enter your question:", "")

if user_input:
    response = chain.invoke({"input": user_input})
    st.subheader("Chatbot's Response:")
    st.write(response)  # Trim to 300 characters
