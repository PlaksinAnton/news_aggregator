from flask import Flask, jsonify, request
import requests
from datetime import datetime
import os


app = Flask(__name__)

log_level = os.getenv("LOG_LEVEL", "INFO")
app.logger.setLevel(log_level)

API_KEY = os.getenv("GUARDIAN_API_KEY")
SEARCH_URL = 'https://content.guardianapis.com/search'
INITIAL_NUMBER_OF_PUBLICATIONS = 30
RESULT_NUMBER_OF_PUBLICATIONS = 5

@app.route('/', methods=['GET'])
def hello_world():
    return "<p>Hello from app!</p>"

@app.route('/get_news', methods=['POST'])
def get_news():
    app.logger.info('/get_news endpoint got called')
    
    request_data = request.get_json()
    request_body = request_data.get("body")
    if request_data is None or request_body is None:
        return jsonify({'error': 'Invalid JSON'}), 400

    try:
        params = { 'q':request_body, 'lang':'en', 'page-size':INITIAL_NUMBER_OF_PUBLICATIONS, 'api-key':API_KEY }
        news_json = requests.get(url = SEARCH_URL, params = params)
    except Exception as e:
        app.logger.error(f"{e}")
        return jsonify({'message': 'Internal news request error'}), 500
    else:
        app.logger.info('successfull news request')

    news_data = news_json.json()
    if news_data.get("response").get("total") is 0:
        app.logger.warning('empty page is returned')
        return jsonify({'empty_page': True, 'lateat_news': []}), 200
    
    try:
        latest_news_data = sorted(
            news_data["response"]["results"], 
            key=lambda x: datetime.strptime(x["webPublicationDate"], "%Y-%m-%dT%H:%M:%SZ"), 
            reverse=True
        )
        latest_news_data = latest_news_data[:RESULT_NUMBER_OF_PUBLICATIONS]
        lateat_news = [
            {
                "publication_date": article["webPublicationDate"],
                "title": article["webTitle"],
                "url": article["webUrl"]
            }
            for article in latest_news_data
        ]
    except Exception as e:
        app.logger.error(f"{e}")
        return jsonify({'message': 'Internal JSON parsing error'}), 500
    else:
        app.logger.info('JSON parsed successfully')
    
    return jsonify({'empty_page': False, 'lateat_news': lateat_news}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8083)
    