from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/health")
def health():
    return "OK"

@app.route("/invoice", methods=["POST"])
def invoice():
    data = request.json
    # simulate billing logic
    return jsonify({"status":"recorded","amount": 100})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
