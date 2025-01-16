from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from rabbitMQ import send_message
from logger_config import logger
import uuid


# Set flask app and cors
app = Flask(__name__)
cors = CORS(app)

# ============ ROUTES ============
@app.route("/ping", methods=["GET", "POST"])
@cross_origin(origins="http://localhost")
def ping():
    return "pong"

@app.route("/user_request", methods=["POST"])
@cross_origin(origins="http://localhost")
def user_request():
    uid = str(uuid.uuid4())
    data = request.json
    try:
        send_message(
            "user_request", 
            {
                "request": data["request"],
                "uid": uid
            }
        )
        return jsonify({"status": "ok", "uid": uid})
    
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})

@app.route("/new_info", methods=["POST"])
@cross_origin(origins="http://localhost")
def new_info():
    data = request.json
    try:
        send_message(
            "new_info",
            {
                "info": data["info"]
            }
        )
        return jsonify({"status": "ok"})
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})


# Run server if the script is run directly
if __name__ == "__main__":
    # Run the Flask development server
    app.run(host="0.0.0.0", port=503, debug=True)