import streamlit as st
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(
    page_title="Chat Widget",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Add custom CSS for centering and styling
st.markdown("""
    <style>
        /* Hide Streamlit default elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {visibility: hidden;}
        
        /* Full viewport height */
        html, body, [class*="css"] {
            height: 100%;
            margin: 0;
            padding: 0;
        }
        
        /* Center the iframe container */
        .iframe-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            width: 100%;
        }
        
        /* Style the iframe */
        .chat-iframe {
            border: none;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 12px;
            overflow: hidden;
        }
    </style>
""", unsafe_allow_html=True)

# Create the HTML for the iframe
chat_html = """
<div class="iframe-container">
    <iframe 
        class="chat-iframe"
        width="640" 
        height="640" 
        src="https://embed.wotnot.io/nhVP8wJYUZam165958636448p4JHOLR5/bot/5bdpjUQkD26L175450164352hOKAHokN?display_header=false&history_retention=false" 
        frameborder="0">
    </iframe>
</div>
"""

# Display the chat widget
components.html(chat_html, height=700)
