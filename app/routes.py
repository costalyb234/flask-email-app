from flask import Blueprint, request, jsonify
from .email_utils import send_email  # or your actual module

main = Blueprint("main", __name__)

@main.route('/send-email', methods=['POST'])
def send_email_route():
    data = request.get_json()

    if not data or not all(k in data for k in ("to", "subject", "message")):
        return jsonify({"error": "Missing 'to', 'subject', or 'message'"}), 400

    try:
        send_email(data['to'], data['subject'], data['message'])
        return jsonify({"status": "Email sent"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
