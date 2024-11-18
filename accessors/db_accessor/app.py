from flask import Flask, g, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import schema as db


app = Flask(__name__)

engine = create_engine('mysql+mysqlconnector://accessor:accessor@localhost/test_db')
Session = sessionmaker(bind=engine)

@app.teardown_appcontext
def close_db_connection(exception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route('/', methods=['GET'])
def hello_world():
    return "<p>Hello from app!</p>"

@app.route('/user/<string:user_name>', methods=['GET']) #, defaults={'user': 'Anton'}
def get_user_info(user_name):
    session = Session()

    user = session.query(db.User).filter(db.User.name == user_name).first()
    if user:
        user_preferences = [preference.preference for preference in user.preferences]
        return jsonify({"Preferences for Anton:": user_preferences})
    else:
        return jsonify({"User": f"{user_name} not found"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082)