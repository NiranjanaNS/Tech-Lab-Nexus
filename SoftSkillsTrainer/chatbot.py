from flask import Flask, request, jsonify
from nltk.chat.util import Chat, reflections

app = Flask(__name__)
pairs = [
    ["(hi|hello|hey)", ["Hello! How can I assist you today with soft skills?"]],
    ["(thank you|thanks)", ["You're welcome!"]],
    ["(goodbye|bye)", ["Goodbye! Take care!"]]
]
chatbot = Chat(pairs, reflections)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = chatbot.respond(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
