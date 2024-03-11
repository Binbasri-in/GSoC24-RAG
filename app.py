import os
from uuid import uuid4
import time
import threading
from flask import Flask, request, jsonify
from queue import Queue

PORT = int(os.environ.get('PORT', 5000))
HOST = os.environ.get('HOST', '127.0.0.1')
SESSION_TTL = int(os.environ.get('SESSION_TTL', 3600))
SESSION_MAX = int(os.environ.get('SESSION_MAX', 10))  # max concurrent sessions

app = Flask(__name__)
sessions = []

class ChatSession:
    def __init__(self):
        self.id = str(uuid4())
        self.timestamp = int(time.time())
        self.messages = Queue()

    def add_message(self, message):
        self.messages.put(message)

    def get_messages(self):
        messages = []
        while not self.messages.empty():
            messages.append(self.messages.get())
        return messages

    def is_expired(self):
        return (self.timestamp + SESSION_TTL) < time.time()

def janitor(sessions):
    while True:
        time.sleep(1)
        sessions[:] = [s for s in sessions if not s.is_expired()]

@app.route('/api/chat', methods=['POST'])
def start_chat():
    if len(sessions) >= SESSION_MAX:
        return jsonify({'message': 'Too many chat sessions - please retry in a minute'}), 500
    session = ChatSession()
    sessions.append(session)
    return jsonify({'session_id': session.id}), 201

@app.route('/api/chat/<session_id>/send', methods=['POST'])
def send_message(session_id):
    session = next((s for s in sessions if s.id == session_id), None)
    if not session:
        return jsonify({'message': 'Chat session not found'}), 404
    message = request.json.get('message')
    if not message:
        return jsonify({'message': 'No message provided'}), 400
    session.add_message({'user': message})
    # Here you can add your chatbot's response logic
    bot_response = f"Echo: {message}"
    session.add_message({'bot': bot_response})
    return jsonify({'message': 'Message sent', 'bot_response': bot_response}), 200

@app.route('/api/chat/<session_id>/messages', methods=['GET'])
def get_messages(session_id):
    session = next((s for s in sessions if s.id == session_id), None)
    if not session:
        return jsonify({'message': 'Chat session not found'}), 404
    messages = session.get_messages()
    return jsonify({'messages': messages}), 200

cleaner = threading.Thread(target=janitor, args=(sessions,))
cleaner.daemon = True
cleaner.start()

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
