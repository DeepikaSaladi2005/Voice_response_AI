from flask import Flask, render_template, request, jsonify
from gtts import gTTS
import openai
import os
import time

app = Flask(__name__)

# Set up OpenAI API key
openai.api_key = "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"

def generate_response(prompt):
    """
    Uses OpenAI's GPT model to generate a response.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        reply = response["choices"][0]["message"]["content"]
        return reply
    except Exception as e:
        return "I'm facing some issues right now."

import time

def text_to_speech(text):
    """
    Converts text to speech and saves it as an MP3 file with a unique name.
    """
    if not text.strip():
        return
    
    timestamp = int(time.time())  # Generate a unique timestamp
    filename = f"static/response_{timestamp}.mp3"  # Unique filename
    
    tts = gTTS(text=text, lang="en", slow=False)
    tts.save(filename)
    
    # Return the filename so it can be sent to the frontend
    return filename

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    
    if not user_message:
        return jsonify({"reply": "Please type something!"})
    
    bot_reply = generate_response(user_message)
    audio_filename = text_to_speech(bot_reply)  # Get the generated filename
    
    return jsonify({"reply": bot_reply, "audio": audio_filename})

if __name__ == "__main__":
    app.run(debug=True)

