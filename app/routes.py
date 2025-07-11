from flask import Blueprint, request, jsonify
import os
from .email_utils import send_email

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({"message": "Flask Email API is running!"})

@main.route('/send-email', methods=['POST'])
def handle_send_email():
    data = request.get_json()
    to = data.get('to')
    subject = data.get('subject')
    body = data.get('body')

    try:
        send_email(to, subject, body)
        return jsonify({"message": "Email sent successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
