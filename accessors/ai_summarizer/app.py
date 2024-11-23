from flask import Flask, g, jsonify, request
from google.protobuf.json_format import MessageToDict
from prompt_model import model
import os

app = Flask(__name__)

log_level = os.getenv("LOG_LEVEL", "INFO")
app.logger.setLevel(log_level)

@app.route('/', methods=['GET'])
def hello_world():
    return "<p>Hello from app!</p>"

@app.route('/summarize_preferences', methods=['POST'])
def summarize():
    app.logger.info('/summarize_preferences endpoint got called')

    raw_preferences_data = request.get_json()
    raw_preferences_body = raw_preferences_data.get("raw_preferences")
    if raw_preferences_data is None:
        return jsonify({'message': 'Invalid JSON'}), 400
    elif not raw_preferences_body.strip():
        return jsonify({'no_topic': True, 'preferences': 'empty preferences'}), 200
    
    try:
        chat_session = model.start_chat(history=[])
        ai_response = chat_session.send_message(raw_preferences_body)
        app.logger.info('answer from AI is received')
        ai_response_dict = MessageToDict(ai_response._result._pb)
    except Exception as e:
        app.logger.error(f"{e}")
        return jsonify({'error': 'Internal chat session error'}), 500

    preferences = (
        ai_response_dict.get("candidates", [{}])[0]
        .get("content", {})
        .get("parts", [{}])[0]
        .get("text")
        .strip()
    )
    if preferences == 'no topic':
        return jsonify({'no_topic': True, 'preferences': preferences}), 200
    elif preferences is None:
        return jsonify({'error': 'Unsuccessful JSON parsing'}), 500
    
    app.logger.info('answer from AI is parsed')
    return jsonify({'no_topic': False, 'preferences': preferences}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8084)
