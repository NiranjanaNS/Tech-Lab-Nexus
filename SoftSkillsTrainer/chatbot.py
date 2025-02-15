```python
from flask import Flask, request, jsonify
from nltk.chat.util import Chat, reflections

app = Flask(__name__)
pairs = [["hi", ["Hello! How can I help you today?"]], ["thank you", ["You're welcome!"]]]
chatbot = Chat(pairs, reflections)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = chatbot.respond(user_input) or "I'm here to help!"
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
```
