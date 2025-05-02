# Integrate our code OpenAi ApiKey

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LangChain_api")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("user", "Question: {question}")
    ]
)

st.title("ChatBot Using LangChain")
st.write("This is a simple chatbot using LangChain and Ollama.")
input_text = st.text_input("Enter your question:")

llm = Ollama(model="gemma3", temperature=0.7)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write("You asked: ", input_text)
    st.write("Answer:", chain.invoke({"question": input_text}))