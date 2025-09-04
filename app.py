import streamlit as st
import streamlit.components.v1 as components

# Set page configuration first
st.set_page_config(
    page_title="Chat Widget",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Add custom CSS
st.markdown("""
    <style>
        /* Hide Streamlit default elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {visibility: hidden;}
        
        /* Basic page styling */
        .stApp {
            background-color: #f0f2f6;
            padding: 20px;
        }
        
        /* Container for the chat */
        .chat-container {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 80vh;
            width: 100%;
        }
        
        /* Style for the chat widget */
        #wotnot-chat-widget {
            width: 100% !important;
            height: 600px !important;
            border: none;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Add title and description
st.title("Welcome to MedSynergy")
st.write("Our virtual assistant is here to help you.")

# Add the WotNot chat widget script
chat_script = """
<script src="https://app.wotnot.io/chat-widget/nhVP8wJYUZam165958636448p4JHOLR5.js" defer></script>
<div id="wotnot-chat-widget"></div>
"""

# Display the chat widget in a container
st.markdown(
    "<div class='chat-container'>" + chat_script + "</div>",
    unsafe_allow_html=True
)
