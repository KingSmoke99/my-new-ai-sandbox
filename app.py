from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json.get('question', '')
    answers = [
        "I think so!", "Maybe...", "No way!", "Ask again later",
        "Yes, definitely!", "Outlook not so good", "Signs point to yes"
    ]
    answer = random.choice(answers)
    
    response = {
        "answer": answer,
        "confidence": "90%",  
        "sources": ["Magic 8-ball", "My Imagination"],
        "discrepancies": "None, because I'm simple!"
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)