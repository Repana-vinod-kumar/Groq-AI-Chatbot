import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

app = Flask(__name__)

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing from .env file")

model = ChatGroq(
    model="openai/gpt-oss-20b",
    groq_api_key=api_key
)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    try:
        data = request.get_json()

        messages = data.get("messages", [])

        if not isinstance(messages, list) or not messages:
            return jsonify({"reply": "Please enter a message."}), 400

        chat_history = [
            SystemMessage(content="You are a helpful AI assistant. Give clear and friendly answers.")
        ]

        for item in messages[-20:]:

            role = item.get("role")
            content = item.get("content", "")

            if not isinstance(content, str) or not content.strip():
                continue

            if role == "user":
                chat_history.append(HumanMessage(content=content))

            elif role == "assistant":
                chat_history.append(AIMessage(content=content))

        if not chat_history or not isinstance(chat_history[-1], HumanMessage):
            return jsonify({"reply": "Please send a valid message."}), 400

        result = model.invoke(chat_history)

        return jsonify({
            "reply": result.content
        })

    except Exception as e:
        print("Chat error:", e)

        return jsonify({
            "reply": "Something went wrong. Please try again."
        }), 500

if __name__ == "__main__":
    app.run(debug=True)