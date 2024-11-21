from flask import Flask, g, jsonify, request
from prompt_model import model

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return "<p>Hello from app!</p>"

@app.route('/summarize_preferences', methods=['POST'])
def summarize():
    data = request.get_json()
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(data["raw_preferences"])

    return jsonify({ "preferences": response }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8084)
