import os
from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize conversation history
conversation = []

def get_gpt_response(user_input):
    message = {"role": "user", "content": user_input}
    conversation.append(message)
    
    response = client.chat.completions.create(
        messages=conversation,
        model="gpt-3.5-turbo"
    )

    assistant_message = response.choices[0].message
    conversation.append(assistant_message)
    
    return assistant_message.content

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    response = get_gpt_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)