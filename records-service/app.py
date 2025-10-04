# records-service/app.py
from flask import Flask, request, jsonify
import os
app = Flask(__name__)

@app.route("/health")
def health():
    return "OK", 200

@app.route("/record", methods=["POST"])
def record():
    data = request.json or {}
    # simulate storing record
    return jsonify({"status":"stored","record": data}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
