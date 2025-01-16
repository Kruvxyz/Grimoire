import time
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from logger_config import logger


if os.getenv('USE_DOTENV', True):
    load_dotenv()

app = Flask(__name__)
if os.getenv("TESTING", None)=="TESTING":
    logger.debug(f"set configuration for testing")
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for testing
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
else:
    logger.debug(f"set configuration for normal use")
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
cors = CORS(app)
    

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(app, model_class=Base)

# ============ MODELS ============ 
class Responses(db.Model):
    __tablename__ = 'responses'

    id = db.Column(db.Integer, primary_key=True)
    last_update = db.Column(db.Integer, nullable=False, default=lambda: int(time.time()))
    uuid = db.Column(db.String(50), nullable=False, unique=True)
    uesr_request = db.Column(db.Text, nullable=True)
    response = db.Column(db.Text, nullable=True)
    reason = db.Column(db.Text, nullable=True)
    status = db.Column(db.Boolean, nullable=False)

    
with app.app_context():
    # db.drop_all()
    logger.debug("Creating tables")
    db.create_all()
    logger.debug("Tables created")


# ============ ROUTES ============
@app.route('/ping')
def ping():
    return "pong"

@app.route('/new_request', methods=['POST'])
@cross_origin(origins="http://localhost")
def new_request():
    data = request.json
    uuid = str(data['uuid'])
    uesr_request = data.get('request', None)
    logger.debug(f"New request: {uuid}")
    try:
        r = Responses(uuid=uuid, uesr_request=uesr_request, status=False)
        db.session.add(r)
        db.session.commit()
        return jsonify({'status': 'ok', 'message': 'Request created', 'uuid': uuid})
    except Exception as e:
        logger.warning(f"Error creating request_uuid={uuid} with error: {e}")
        return jsonify({'status': 'error', 'message': e})

@app.route('/update_response', methods=['POST'])
@cross_origin(origins="http://localhost")
def update_response():
    data = request.get_json()
    uuid = str(data['uuid'])
    response = data['response']
    reason = data.get('reason', None)
    logger.debug(f"Updating response: {uuid}")
    try:
        r = Responses.query.filter_by(uuid=uuid).first()
        r.response = response
        r.reason = reason
        r.status = True
        db.session.commit()
        return jsonify({'status': 'ok', 'message': 'Response updated', 'uuid': uuid})
    except Exception as e:
        logger.warning(f"Error updating response_uuid={uuid} with error: {e}")
        return jsonify({'status': 'error', 'message': e})

@app.route('/read_response', methods=['GET'])
@cross_origin(origins="http://localhost")
def read_response():
    uuid = request.args.get('uuid')
    logger.debug(f"Reading response: {uuid}")
    r = Responses.query.filter_by(uuid=uuid).first()
    if r is None:
        return jsonify({'status': 'error', 'message': 'Response not found'})
    return jsonify({'status': 'ok' if r.status else 'processing', 'response': r.response, 'reason': r.reason})

# Run server if the script is run directly
if __name__ == '__main__':
    # Run the Flask development server
    app.run(host="0.0.0.0", port=5050, debug=True)