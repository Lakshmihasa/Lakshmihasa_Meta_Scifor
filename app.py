import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai
import time
from datetime import datetime

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Chat Deep!",
    page_icon="🐠",  # Favicon emoji to match the underwater theme
    layout="centered",  # Page layout option
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Sidebar with GIF and Chatbot Connection Booster
st.sidebar.title("Chat Deep: Exploring AI Under the Sea 🌊🧠")

# Sidebar GIF
gif_url = "C:/Users/hp/Mini_Project_2/fish.gif"
st.sidebar.image(gif_url, use_column_width=True)

# Display daily tip in sidebar
def get_daily_tip():
    # Example list of tips with emojis
    tips = [
        "💧 Tip: Remember to stay hydrated and take breaks while coding!",
        "📂 Tip: Use version control to track changes in your code.",
        "🧹 Tip: Write clean and readable code for better maintainability.",
        "🛠️ Tip: Test your code thoroughly to catch bugs early.",
        "🚀 Tip: Keep learning and stay updated with new technologies."
    ]
    # Select a tip based on the current day of the year
    day_of_year = datetime.now().timetuple().tm_yday
    return tips[day_of_year % len(tips)]

st.sidebar.subheader("Daily Tip 💡")
st.sidebar.write(get_daily_tip())

# Check if chat input should be shown
if 'show_chat_input' in st.session_state and st.session_state.show_chat_input:
    st.text_input("Ask Gemini-Pro...", key="user_input", placeholder="Type your message here...")

# Live bubbles background
st.markdown(
    """
    <style>
    html, body {
        height: 100%;
        margin: 0;
        overflow: hidden;
    }
    body {
        background-color: #2c3e50;  /* Dark blue ocean */
        color: #ecf0f1;  /* Soft white text */
        position: relative;  /* Position relative for absolute positioning of bubbles */
    }
    .bubble {
        position: fixed;
        background: #3498db;
        border-radius: 50%;
        opacity: 0.7;
        animation: rise 10s infinite ease-in;
        z-index: 0;  /* Behind other content */
    }
    @keyframes rise {
        0% { transform: translateY(0); }
        100% { transform: translateY(-100vh); }
    }

    /* Fish animation */
    .fish {
        position: fixed;
        width: 50px;
        animation: swim 10s infinite ease-in-out;
        z-index: 1;  /* In front of bubbles */
    }
    @keyframes swim {
        0% { transform: translateX(-100px) rotateY(0deg); }
        50% { transform: translateX(100vw) rotateY(0deg); }
        50.01% { transform: translateX(100vw) rotateY(180deg); }
        100% { transform: translateX(-100px) rotateY(180deg); }
    }

    /* Custom colors for chat messages and input */
    .chat-message {
        background-color: #f8bbd0; /* Light pink background for chatbot messages */
        border-radius: 10px;
        padding: 10px;
        margin: 5px 0;
        max-width: 80%;
    }
    .user-message {
        background-color: #add8e6; /* Light blue background for user messages */
        border-radius: 10px;
        padding: 10px;
        margin: 5px 0;
        max-width: 80%;
        align-self: flex-end;
    }
    .chat-input {
        border: 2px solid #87CEEB; /* Light blue border for input box */
        border-radius: 5px;
        padding: 10px;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to create enhanced bubbles all over the page and fish
def create_underwater_elements():
    import random
    bubble_template = """
    <div class="bubble" style="width: {size}px; height: {size}px; left: {left}%; bottom: {bottom}%; animation-duration: {duration}s;"></div>
    """
    fish_template = """
    <div class="fish" style="top: {top}%; left: {left}%;"><img src="https://img.icons8.com/color/48/000000/fish.png" alt="fish"/></div>
    """

    bubbles_html = "".join([bubble_template.format(
        size=random.randint(15, 40),  # Random bubble size between 15px and 40px
        left=random.uniform(0, 100),  # Random horizontal position between 0% and 100%
        bottom=random.uniform(0, 100),  # Random vertical position between 0% and 100%
        duration=random.uniform(8, 20)  # Random duration between 8s and 20s
    ) for _ in range(30)])  # Generate 30 bubbles
    
    fish_html = "".join([fish_template.format(top=top, left=left)
                         for top, left in [(15, -20), (35, -30), (55, -50), (75, -70)]])

    st.markdown(bubbles_html + fish_html, unsafe_allow_html=True)

create_underwater_elements()

# Display the chatbot's title on the page
st.title("Chat Deep 🌊")

# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        # Apply custom class based on message role
        class_name = "chat-message" if message.role == "model" else "user-message"
        st.markdown(f'<div class="{class_name}">{message.parts[0].text}</div>', unsafe_allow_html=True)

# Display a clock in the top-right corner
current_time = datetime.now().strftime("%H:%M:%S")
st.markdown(
    f"""
    <div style="position: fixed; top: 10px; right: 10px; font-size: 16px; color: #ecf0f1; z-index: 2;">
        {current_time}
    </div>
    """,
    unsafe_allow_html=True
)

# Input field for user's message
user_prompt = st.text_input("Ask Chat Deep...", key="user_input", placeholder="Type your message here...")
if user_prompt:
    # Add user's message to chat and display it
    st.markdown(f'<div class="user-message">{user_prompt}</div>', unsafe_allow_html=True)

    # Display a progress bar synced with response time
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.02)  # Simulating response time, adjust as needed
        progress_bar.progress(percent_complete + 1)

    # Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display Gemini-Pro's response
    st.markdown(f'<div class="chat-message">{gemini_response.text}</div>', unsafe_allow_html=True)
