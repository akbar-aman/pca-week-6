from flask import Flask, request, jsonify
import uuid
from datetime import datetime

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

@app.route('/healthz', methods=['GET'])
def healthz():
    """Endpoint for GCP health checks."""
    return jsonify({'status': 'healthy'}), 200

@app.route("/invoice", methods=["POST"])
def invoice():
    data = request.json or {}

    # extract fields (with defaults)
    customer = data.get("customer", "unknown")
    amount = data.get("amount", 0)

    # simulate invoice generation
    invoice_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()

    return jsonify({
        "status": "billed",
        "invoice_id": invoice_id,
        "customer": customer,
        "amount": amount,
        "currency": "USD",
        "timestamp": timestamp
    }), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

