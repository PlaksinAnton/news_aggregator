from flask import Flask, g, jsonify, request
import os
from connectors import connect_to_ai_summarizer, connect_to_news_collector, connect_to_message_handler
from response_handlers import handle_response

app = Flask(__name__)

log_level = os.getenv("LOG_LEVEL", "INFO")
app.logger.setLevel(log_level)

@app.route('/', methods=['GET'])
def hello_world():
    return "<p>Hello from app!</p>"

@app.route('/request_queue', methods=['POST'])
def request_queue():
    app.logger.info('/request_queue endpoint got called')

    user_data = request.get_json()
    raw_preferences = user_data.get("raw_preferences")
    user_email = user_data.get("email")
    if raw_preferences is None or user_email is None:
        app.logger.warning('endpoint got invalid request JSON')
        return jsonify({'message': 'Invalid JSON'}), 400
    
    ai_summarizer_response = connect_to_ai_summarizer(raw_preferences)
    result = handle_response(app.logger, ai_summarizer_response, 'AI summarizer')
    if isinstance(result, tuple): return result # Check if it's an error response
    ai_summarizer_response = result

    if ai_summarizer_response['no_topic'] == True:
        return jsonify({'error': "Preferenses not found, enter another"}), 422
    
    news_collector_response = connect_to_news_collector(ai_summarizer_response['preferences'])
    result = handle_response(app.logger, news_collector_response, 'news collector')
    if isinstance(result, tuple): return result # Check if it's an error response
    news_collector_response = result

    if news_collector_response['empty_page'] == True:
        return jsonify({'error': "No suitable news found"}), 422
     
    subject = "Your personal news digest"
    email_body = ""
    for news in news_collector_response['lateat_news']:
        title = f"<b><a href='{news['url']}'>{news['title']}</a></b>"
        publication_date = news['publication_date']
        email_body += f"{title}<br>{publication_date}<br><br>"
    
    message_handler_response = connect_to_message_handler(user_email, subject, email_body)
    result = handle_response(app.logger, message_handler_response, 'message handler')
    if isinstance(result, tuple): return result # Check if it's an error response

    return jsonify({'message': 'Email sent!'}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082)
