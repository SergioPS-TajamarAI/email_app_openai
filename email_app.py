import streamlit as st
from openai import AzureOpenAI
import os
from dotenv import load_dotenv



def setup_openai_client():
    load_dotenv(override=True)
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-02-15-preview"
    )
    return client

def generate_summary(client, email_text, temperature=0.0):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that must summarize emails."},
            {"role": "user", "content": email_text}
        ],
        temperature = temperature
    )
    return response

def generate_answer(client, email_text, temperature=0.0):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates responses to emails."},
            {"role": "user", "content": email_text}
        ],
        temperature = temperature
    )
    return response


client = setup_openai_client()

st.title("Email App")

# Text area for email input
email_input = st.text_area("Enter your email here:")

# Buttons for generating summary and answer
if st.button("Generate Summary"):
    summary_response = generate_summary(client, email_input)
    st.write(summary_response.choices[0].message.content)

if st.button("Generate Answer"):
    answer_response = generate_answer(client, email_input)
    st.write(answer_response.choices[0].message.content)