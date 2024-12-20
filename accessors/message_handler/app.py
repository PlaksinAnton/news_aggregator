from flask import Flask, g, jsonify, request
import mailer
import os

app = Flask(__name__)

log_level = os.getenv("LOG_LEVEL", "INFO")
app.logger.setLevel(log_level)
# log_handler = logging.handlers.RotatingFileHandler('app.log', maxBytes=5*1024*1024, backupCount=2)

@app.route('/', methods=['GET'])
def hello_world():
    return "<p>Hello from app!</p>"

@app.route('/send_message', methods=['POST'])
def send_message():
    app.logger.info('/send_message endpoint got called')
    
    message_data = request.get_json()
    if message_data is None:
        app.logger.warning('endpoint got invalid request JSON')
        return jsonify({'message': 'Invalid JSON'}), 400

    try:
        service = mailer.authenticate_gmail()
    except Exception as e:
        app.logger.error(f"while authentication: {e}")
        return jsonify({'error': 'Internal email api authentication error'}), 500
    else:
        app.logger.info('successfull gmail authentication')

    sender = "aplaksin691@gmail.com"
    recipient = message_data.get("recipient")
    subject = message_data.get("subject")
    body = message_data.get("body")

    if body is None or subject is None or recipient is None:
        app.logger.warning('some JSON fields are empty')
        return jsonify({'message': 'JSON does not contain all necessary fields'}), 400
    app.logger.info('JSON parsing is done')

    try:
        mailer.send_email(service,
                          sender,
                          recipient,
                          subject, 
                          body)
    except Exception as e:
        app.logger.error(f"while sending email: {e}")
        return jsonify({'error': 'Internal email api sending error'}), 500
    else:
        app.logger.info('email is sent successfully')

    return jsonify({'message': 'Success'}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8085)
