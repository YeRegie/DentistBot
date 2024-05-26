#!/usr/bin/env python
# coding: utf-8

# In[8]:


import streamlit as st
import os
import google.generativeai as genai
import time


# In[9]:


# Load API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")

if api_key is None:
    st.error("API key is not set. Please set the GEMINI_API_KEY environment variable.")
else:
    genai.configure(api_key=api_key)

if 'chat_session' not in st.session_state:
    model = genai.GenerativeModel('gemini-1.5-pro')
    st.session_state.chat_session = model.start_chat()
    st.session_state.chat_history = []


# In[10]:


# See if there's an ongoing chat session; if not, start a new one.
#if 'chat_session' not in st.session_state:
 #   model = genai.GenerativeModel('gemini-1.5-pro')
 #   st.session_state.chat_session = model.start_chat()
 #   st.session_state.chat_history = []  

def handle_chat(question):
    try:
         # add an introduction to our response to make it more welcoming for users.
        intro_response = "Hi there! I'm Gigi, your AI dentist chatbot here to help you evaluate your dental symptoms. Let's work through this together."
        # Sends the user's question to the chat API and gets a response.
        response = st.session_state.chat_session.send_message(question)
        # Puts together a friendly introduction, the API's response, and a prompt to keep the conversation going.
        full_response = f"{intro_response} {response.text} Is there anything else I can assist you with regarding your dental health?"

        # Appends the question and response to the session's history for display.
        st.session_state.chat_history.append({"type": "Question", "content": question})
        st.session_state.chat_history.append({"type": "Response", "content": full_response})
        return full_response
    except Exception as e:
        # Handles exceptions by displaying an error message and returning a fallback message.
        st.error(f"An error occurred: {str(e)}")
        time.sleep(1)  
        return "An error occurred. Please try again."


# In[11]:


def display_history():
    with st.container():  # Sets up a scrollable area for showing past conversations in the chat.
        for entry in st.session_state.chat_history:
                # Formats and Displays user inquiries.
            if entry['type'] == "Question":
                st.markdown(f"<p style='font-size:16px; font-weight:bold;'>Your Inquiry:</p><p style='font-size:16px;'>{entry['content']}</p>", unsafe_allow_html=True)
            elif entry['type'] == "Response":
                # Formats and Displays responses from the chatbot.
                formatted_response = entry['content'].replace("**", "<b>").replace("<b>", "</b>")
                st.markdown(f"<p style='font-size:16px; font-weight:bold;'>Response from Gigi:</p><p style='font-size:16px;'>{formatted_response}</p>", unsafe_allow_html=True)


# In[12]:


# Streamlit App setup
st.set_page_config(page_title="GGSS - Gigi's Grin Guru")
st.header("Your Chatbot for Dental Wellness")

# Creator Info
with st.expander("Display info about the creator"):
    text = """Regino C. Gallena\n
    BSCS 3A AI
    Final Project for CCS 229 - Intelligent Systems
    Bachelor of Science in Computer Science
    College of Information and Communications Technology
    West Visayas State University
    """
    st.write(text)


# In[13]:


# A comprehensive guide on how to use the GGSS - Gigi's Smile Support
with st.expander("Gigi's Smile Support: Getting Started "):
    text = """Welcome to GGSS  - Gigi's Smile Support! Throughout this chat, Gigi will serve as your AI dental assistant. This chatbot is crafted to offer essential health insights and assist you with basic questions regarding symptoms, dental conditions, and wellness tips. Let's get started with these straightforward instructions for engaging with the chatbot:

1. **Launching the Chat**\n
Upon opening the application, you'll encounter a text input field labeled **"Enter your dental inquiry here:"**\n. This is where you'll pose your questions.\n
2. **Submitting Your Inquiry**\n
Enter your question in the text box, ensuring it remains focused on dental symptoms or health conditions. For instance, rather than stating **"I feel unwell,"** you could inquire, **"What are common causes of tooth sensitivity?"** or simply state your symptom, such as **"Toothache."** Optionally, you can include any suspected causes for a more precise response.
Press the "Ask Gigi" button to send your question.\n
3. **Viewing Responses**\n
Once you've submitted your question, Gigi, your AI dental assistant, will process your query and provide a response below the input field.\n
4. **Continuing the Conversation**\n
Should you have additional questions for Gigi, simply type them into the text box and click **"Ask Gigi"** again. Each new and previous conversation will be archived in a scrollable container, facilitating easy review of past interactions.\n
5. **Resetting the Conversation**\n
To initiate a new session and clear all prior conversations, utilize the **"Reset Conversation"** button. This action will erase all chat history, allowing you to commence anew.\n
"""
    st.markdown(text, unsafe_allow_html=True)


# In[14]:


# Main interaction area 
user_input = st.text_input("Please type your dental-related questions here:", key="user_query")
if st.button("Ask Gigi"):
    if user_input:
        # See if the question already mentions specific words we're looking for.
        if 'causes' in user_input.lower() or 'treatments' in user_input.lower():
            response_text = handle_chat(user_input) 
        else:
            # help the user narrow down their question to make it clearer.
            refined_query = f"What are some typical causes and treatments for {user_input}?"
            response_text = handle_chat(refined_query)
        display_history()
    else:
        st.warning("Kindly input your inquiry regarding dental health information.")

# Button to reset the conversation, clearing all history and starting a new session.
if st.button("Reset Conversation"):
    model = genai.GenerativeModel('gemini-1.5-pro')
    st.session_state.chat_session = model.start_chat()
    st.session_state.chat_history = []  # This clears the history


# In[ ]:





# In[ ]:




