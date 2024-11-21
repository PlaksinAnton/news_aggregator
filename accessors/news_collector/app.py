from flask import Flask, g, jsonify
import requests
import os


app = Flask(__name__)

api_key = os.getenv("GUARDIAN_API_KEY")

# @app.before_request
# def setup_session():

# @app.teardown_appcontext
# def shutdown_session(exception=None):

@app.route('/', methods=['GET'])
def hello_world():
    return "<p>Hello from app!</p>"

@app.route('/request/<string:request>', methods=['GET'])
def get_api_data(request):
    base_url = 'https://content.guardianapis.com/search'
    params = { 'q':request, 'api-key':api_key }
    r = requests.get(url = base_url, params = params)
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8083)