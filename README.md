# TalentScout Hiring Assistant 🤖

An interactive AI-powered Streamlit chatbot that simulates a mini technical recruiter. It gathers candidate details conversationally and generates personalized technical interview questions based on selected tech stacks (Python, React, MySQL, etc.). Powered by the quantized LLaMA 2 7B model and fully runs on CPU – no GPU required!


---

## 🚀 Features

- Conversational form for collecting user details
- Dynamic prompt creation based on selected tech stack
- CPU-based inference using quantized LLaMA 2 7B model
- Lightweight deployment using Streamlit
- Facebook-like chat styling using Streamlit’s `chat_message`

---

## 🔧 Installation Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Mothi-S/TalentScout-Hiring-Assistant-chatbot.git
cd TalentScout-Hiring-Assistant-chatbot

2. Set Up Virtual Environment

python -m venv venv
venv\Scripts\activate  # For Windows
# OR
source venv/bin/activate  # For macOS/Linux

3. Install Dependencies

pip install -r requirements.txt

4. Download and Add the LLaMA 2 Model

Download the quantized LLaMA 2 7B model file (llama-2-7b-chat.ggmlv3.q8_0.bin) from Hugging Face:

📥 Download from TheBloke's HuggingFace Repo

Create a folder named models/ in the project directory and place the .bin file inside it:

5. Run the Application

streamlit run app.py


