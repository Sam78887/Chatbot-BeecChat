from flask import Flask, request, jsonify
from flask_cors import CORS  # Import the CORS package

app = Flask(__name__)

# Enable CORS for all routes and all domains
CORS(app)  # This will allow all domains to access all routes







import os
import google.generativeai as genai



# Configure the API key for Gemini
os.environ["GEMINI_API_KEY"] = "AIzaSyDoeGQM9-y7W2z8rOESzLH46h2Ziv8rk14"
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "max_output_tokens": 2048,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
)

chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [
                "Your name is BeeChat,a chatbot.You will chat with user on anything.This is Samaresh's Linkedin Profile url-\"www.linkedin.com/in/samaresh-dutta-926643225\" .Your deployment/implementation is done by Samaresh Dutta,an aspiring engineer from India.This is Samaresh's Social Account or Job Profile url/link-\"www.linkedin.com/in/samaresh-dutta-926643225\".This is Samaresh's GitHub Profile link-\"https://github.com/Sam78887\".Samaresh studies in Techno Main Salt Lake,pursuing B.tech in Information Technology.Samaresh is interested in web development,chatbot development and various other projects.You will remember chat history of that person while continuing chat.You will be polite with user.",
            ],
        },
        {
            "role": "model",
            "parts": [
                "Hello!😊 My name is BeeChat, I am a chatbot 😄 . I am happy to chat with you about anything you like.",
            ],
        },
    ]
)


@app.route("/chat", methods=["POST"])
def chat():
    
    user_input = request.json.get("message")
    if user_input:
        response = chat_session.send_message(user_input)
        return jsonify({"response": response.text})
    else:
        return jsonify({"error": "No message provided"}), 400


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")



