import streamlit as st
from llm_loader import load_llm
from prompt_generator import build_prompt

st.set_page_config(page_title="Hiring Assistant", layout="centered")

# Styles
st.markdown("""
<style>
.chat-bubble-user {
    background-color: #0084FF;
    color: white;
    padding: 12px 16px;
    border-radius: 18px;
    max-width: 70%;
    margin-left: auto;
    margin-bottom: 8px;
    text-align: left;
}
.chat-bubble-bot {
    background-color: #f1f0f0;
    color: black;
    padding: 12px 16px;
    border-radius: 18px;
    max-width: 70%;
    margin-right: auto;
    margin-bottom: 8px;
    text-align: left;
}
</style>
""", unsafe_allow_html=True)

# Initialize session
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.user_data = {}
    st.session_state.llm = load_llm()
    st.session_state.greeted = False
    st.session_state.questions_generated = False
    st.session_state.chat_ended = False

# Questions
fields = [
    ("full_name", "Hi! I'll collect a few details.\nWhat's your full name?"),
    ("email", "Thanks, {full_name}! What's your email address?"),
    ("phone", "Got it. What's your phone number?"),
    ("experience", "How many years of experience do you have?"),
    ("position", "What position are you applying for?"),
    ("location", "Where are you currently located?"),
    ("tech_stack", "Great. What is your tech stack? (e.g., Python, React, MySQL)")
]

# Title
st.markdown("<h1 style='text-align: center;'>🤖 TalentScout Hiring Chatbot</h1>", unsafe_allow_html=True)

# Greeting
if not st.session_state.greeted:
    with st.chat_message("assistant"):
        st.markdown("""
        👋 **Welcome to the TalentScout Hiring Assistant!**  
        I'm here to help you get prepared for your next tech interview.  
        I’ll ask you a few quick questions to understand your profile and then generate customized technical questions based on your tech stack. 🚀
        """)
    st.session_state.greeted = True

# Display previous Q&A
for idx in range(st.session_state.step):
    key, question = fields[idx]
    formatted_question = question.format(**st.session_state.user_data)

    with st.chat_message("assistant"):
        st.markdown(f"<div class='chat-bubble-bot'>{formatted_question}</div>", unsafe_allow_html=True)
    with st.chat_message("user"):
        st.markdown(f"<div class='chat-bubble-user'>{st.session_state.user_data[key]}</div>", unsafe_allow_html=True)

# Ask current question
if st.session_state.step < len(fields):
    key, question = fields[st.session_state.step]
    formatted_question = question.format(**st.session_state.user_data)

    with st.chat_message("assistant"):
        st.markdown(f"<div class='chat-bubble-bot'>{formatted_question}</div>", unsafe_allow_html=True)

    user_input = st.chat_input("Your answer")
    if user_input:
        st.session_state.user_data[key] = user_input
        st.session_state.step += 1
        st.rerun()

# Generate interview questions
elif not st.session_state.questions_generated:
    with st.chat_message("assistant"):
        st.markdown("<div class='chat-bubble-bot'>✅ <strong>Thank you! Here's a summary of your details:</strong></div>", unsafe_allow_html=True)
        for label, value in st.session_state.user_data.items():
            st.markdown(f"<div class='chat-bubble-bot'><strong>{label.replace('_', ' ').title()}</strong>: {value}</div>", unsafe_allow_html=True)

        tech_stack = st.session_state.user_data["tech_stack"]
        prompt = build_prompt(tech_stack)
        st.markdown(f"<div class='chat-bubble-bot'>🔍 <strong>Generating interview questions for:</strong> `{tech_stack}`...</div>", unsafe_allow_html=True)

        response = st.session_state.llm(prompt)
        st.markdown(f"<div class='chat-bubble-bot'>🧪 <strong>Here are your questions:</strong><br><br>{response}</div>", unsafe_allow_html=True)

        # ✅ Store response in session state
        st.session_state.generated_response = response

    st.session_state.questions_generated = True

# Show generated response again if already generated
elif st.session_state.questions_generated:
    with st.chat_message("assistant"):
        st.markdown("<div class='chat-bubble-bot'>✅ <strong>Here’s a summary of your details:</strong></div>", unsafe_allow_html=True)
        for label, value in st.session_state.user_data.items():
            st.markdown(f"<div class='chat-bubble-bot'><strong>{label.replace('_', ' ').title()}</strong>: {value}</div>", unsafe_allow_html=True)

        tech_stack = st.session_state.user_data["tech_stack"]
        st.markdown(f"<div class='chat-bubble-bot'>🧪 <strong>Here are your questions for:</strong> `{tech_stack}`</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='chat-bubble-bot'>{st.session_state.generated_response}</div>", unsafe_allow_html=True)

    # Final chat input
    if not st.session_state.chat_ended:
        user_final_input = st.chat_input("Type 'end' to finish the chat")

        if user_final_input:
            if user_final_input.strip().lower() == "end":
                with st.chat_message("user"):
                    st.markdown(f"<div class='chat-bubble-user'>end</div>", unsafe_allow_html=True)
                with st.chat_message("assistant"):
                    st.markdown("<div class='chat-bubble-bot'>🎉 Thank you for using the TalentScout Hiring Assistant! Best of luck with your interview! 👋</div>", unsafe_allow_html=True)
                st.session_state.chat_ended = True
            else:
                with st.chat_message("user"):
                    st.markdown(f"<div class='chat-bubble-user'>{user_final_input}</div>", unsafe_allow_html=True)
                with st.chat_message("assistant"):
                    st.markdown("<div class='chat-bubble-bot'>Please type <strong>'end'</strong> to finish the chat.</div>", unsafe_allow_html=True)



# Handle end message
if st.session_state.questions_generated and not st.session_state.chat_ended:
    user_final_input = st.chat_input("Type 'end' to finish the chat")

    if user_final_input:
        if user_final_input.strip().lower() == "end":
            with st.chat_message("user"):
                st.markdown(f"<div class='chat-bubble-user'>end</div>", unsafe_allow_html=True)
            with st.chat_message("assistant"):
                st.markdown("<div class='chat-bubble-bot'>🎉 Thank you for using the TalentScout Hiring Assistant! Best of luck with your interview! 👋</div>", unsafe_allow_html=True)
            st.session_state.chat_ended = True
        else:
            with st.chat_message("user"):
                st.markdown(f"<div class='chat-bubble-user'>{user_final_input}</div>", unsafe_allow_html=True)
            with st.chat_message("assistant"):
                st.markdown("<div class='chat-bubble-bot'>Please type <strong>'end'</strong> to finish the chat.</div>", unsafe_allow_html=True)
