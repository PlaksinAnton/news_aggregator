from flask import Flask, g, jsonify


app = Flask(__name__)

# @app.before_request
# def setup_session():

# @app.teardown_appcontext
# def shutdown_session(exception=None):

@app.route('/', methods=['GET'])
def hello_world():
    return "<p>Hello from app!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8083)