import streamlit as st
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(
    page_title="MedSynergy Chat",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Add WotNot chat widget script
chat_script = """
<script src="https://app.wotnot.io/chat-widget/nhVP8wJYUZam165958636448p4JHOLR5.js" defer></script>
"""

# Display the chat widget
components.html(chat_script, height=0)
