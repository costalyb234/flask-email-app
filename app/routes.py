from flask import Flask, request, jsonify
from email_utils import send_email  # replace with actual import

app = Flask(__name__)

@app.route('/send-email', methods=['POST'])
def send():
    try:
        data = request.get_json()

        to = data.get('to')
        subject = data.get('subject')
        body = data.get('message')

        if not all([to, subject, body]):
            return jsonify({"error": "Missing 'to', 'subject', or 'message'"}), 400

        send_email(to, subject, body)
        return jsonify({"success": True}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
