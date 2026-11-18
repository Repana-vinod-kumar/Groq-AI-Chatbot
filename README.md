# 🤖 Groq AI Chatbot

An intelligent AI-powered chatbot built using Python, Flask, Groq API, and LangChain. This application provides real-time conversational responses using Large Language Models (LLMs) through an interactive and user-friendly web interface.

## 🚀 Project Overview

Groq AI Chatbot is a web-based conversational assistant designed to understand user queries and generate intelligent responses using advanced AI language models.

The application uses Flask as the backend framework and Groq API for AI-powered response generation. LangChain helps integrate and manage interactions with the language model.

## ✨ Key Features

- 🤖 AI-powered intelligent conversations.
- ⚡ Fast response generation using Groq API.
- 💬 Interactive chatbot interface.
- 🧠 Large Language Model (LLM) integration.
- 🔗 LangChain integration.
- 🌐 Web-based user interface.
- 🐍 Python Flask backend.
- 🔐 Secure API key management using environment variables.
- 📱 User-friendly chat experience.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework |
| Groq API | AI response generation |
| LangChain | LLM integration |
| HTML | Web page structure |
| CSS | User interface styling |
| JavaScript | Frontend interaction |
| Python-dotenv | Environment variable management |

## 📂 Project Structure

```text
Groq-AI-Chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── templates/
│   └── index.html
│
└── static/
    ├── css/
    ├── js/
    └── images/
```

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/Repana-vinod-kumar/Groq-AI-Chatbot.git
```

### Step 2: Navigate to Project Folder

```bash
cd Groq-AI-Chatbot
```

### Step 3: Create Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
pip install flask langchain langchain-groq python-dotenv
```

### Step 6: Configure API Key

Create a `.env` file in the project root directory.

Add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from the Groq Console:

https://console.groq.com/keys

**Important:** Never upload your `.env` file or API key to GitHub.

### Step 7: Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## 🔮 Future Enhancements

- User authentication and registration.
- Chat history management.
- Voice-based chatbot interaction.
- Database integration.
- Document-based question answering.
- Multiple AI model support.

## 👨‍💻 Developer

**Repana Vinod Kumar**

GitHub: https://github.com/Repana-vinod-kumar

## 📄 License

This project is developed for educational and learning purposes.
