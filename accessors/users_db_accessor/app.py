from flask import Flask, g, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import schema as db


app = Flask(__name__)

engine = create_engine('mysql+mysqlconnector://accessor:accessor@users_db/users_db') # //username:password@host/database_name
Session = sessionmaker(bind=engine)

@app.before_request
def setup_session():
    if not hasattr(g, 'db_session'):
        g.db_session = Session()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session = getattr(g, 'db_session', None)
    if db_session:
        db_session.close()

@app.route('/', methods=['GET'])
def hello_world():
    return "<p>Hello from app!</p>"

@app.route('/user/<string:user_name>', methods=['GET']) #, defaults={'user': 'Anton'}
def get_user_info(user_name):
    session = getattr(g, 'db_session')

    user = session.query(db.User).filter(db.User.name == user_name).first()
    if user:
        user_preferences = [preference.preference for preference in user.preferences]
        session.close()
        return jsonify({"Preferences for Anton:": user_preferences})
    else:
        session.close()
        return jsonify({"User": f"{user_name} not found"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082)