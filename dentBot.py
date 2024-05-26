import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
import time

# Load API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API with the API key loaded from environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

if 'chat_session' not in st.session_state:
    model = genai.GenerativeModel('gemini-1.5-pro')
    st.session_state.chat_session = model.start_chat()
    st.session_state.chat_history = []
    st.session_state.interaction_count = 0
    st.session_state.step = 0
    st.session_state.dental_history = ""
    st.session_state.dental_issue = ""

def handle_chat(question):
    try:
        response = st.session_state.chat_session.send_message(question)
        st.session_state.chat_history.append({"type": "Question", "content": question})
        st.session_state.chat_history.append({"type": "Response", "content": response.text})
        st.session_state.interaction_count += 1
        return response.text
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        time.sleep(1)
        return "An error occurred. Please try again."

def display_history():
    with st.container():
        for entry in st.session_state.chat_history:
            if entry['type'] == "Question":
                st.markdown(f"<p style='font-size:16px; font-weight:bold;'>Your Inquiry:</p><p style='font-size:16px;'>{entry['content']}</p>", unsafe_allow_html=True)
            elif entry['type'] == "Response":
                formatted_response = entry['content'].replace("**", "<b>").replace("<b>", "</b>")
                st.markdown(f"<p style='font-size:16px; font-weight:bold;'>Response from Gigi:</p><p style='font-size:16px;'>{formatted_response}</p>", unsafe_allow_html=True)

st.set_page_config(page_title="GGSS - Gigi's Grin Guru")
st.header("Gigi's Smile Support: Grin Guru")
st.markdown("**Your Chatbot for Dental Wellness**\n")

# Info about the Developer section
st.markdown("**Info about the Project**")
developer_info = """**Name:** Regino C. Gallena\n
**Section:** BSCS 3A-AI\n

**Details:** A final project requirement for completion of the CCS 229 - Intelligent Systems
course in the Bachelor of Science in Computer Science program 
at the College of Information and Communications Technology, West Visayas State University.
"""
st.write(developer_info)

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
        if 'reasons' in user_input.lower() or 'treatments' in user_input.lower():
            response_text = handle_chat(user_input) 
        else:
            # help the user narrow down their question to make it clearer.
            refined_query = f"What are some typical reasons, causes and treatments for {user_input}?"
            response_text = handle_chat(refined_query)
        display_history()
    else:
        st.warning("Kindly input your inquiry regarding dental health information.")

# Button to reset the conversation, clearing all history and starting a new session.
if st.button("Reset Conversation"):
    model = genai.GenerativeModel('gemini-1.5-pro')
    st.session_state.chat_session = model.start_chat()
    st.session_state.chat_history = []  # This clears the history
