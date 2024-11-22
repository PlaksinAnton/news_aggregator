from flask import Flask, g, jsonify, request
import mailer

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return "<p>Hello from app!</p>"

@app.route('/send_message', methods=['POST'])
def send_message():
    message_data = request.get_json()
    service = mailer.authenticate_gmail()
    sender = "aplaksin691@gmail.com"

    mailer.send_email(service, 
                      sender, 
                      message_data.get("recipient"), 
                      message_data.get("subject"), 
                      message_data.get("body"))
    return jsonify({'message': 'Success'}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8084)
