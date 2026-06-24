import os
import time
import requests
import base64
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# ==========================================
# PAYHERO CONFIGURATION
# ==========================================
API_USERNAME = os.getenv("API_USERNAME")
API_PASSWORD = os.getenv("API_PASSWORD")
ACCOUNT_ID = os.getenv("ACCOUNT_ID")
CHANNEL_ID = os.getenv("CHANNEL_ID")
PUBLIC_URL = os.getenv("PUBLIC_URL") 
PAYHERO_API_URL = "https://backend.payhero.co.ke/api/v2/payments"

# Store payment statuses temporarily (In production, use Redis or a Database)
payment_status_store = {}

# Auth Setup
credentials = f"{API_USERNAME}:{API_PASSWORD}"
encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Basic {encoded_credentials}'
}

# ==========================================
# FRONT-END ROUTES
# ==========================================
@app.route('/')
def home():
    return render_template('index.html')

# ==========================================
# BACKEND API ROUTES
# ==========================================
@app.route('/api/initiate-payment', methods=['POST'])
def initiate_payment():
    data = request.json
    phone = data.get('phone')
    plan = data.get('plan')
    
    if plan == 'basic': amount, ref_prefix = 200, "BAS"
    elif plan == 'premium': amount, ref_prefix = 500, "PREM"
    elif plan == 'premium-plus': amount, ref_prefix = 1500, "PLUS"
    else: return jsonify({"success": False, "error": "Invalid plan selected"}), 400

    external_ref = f"{ref_prefix}-{int(time.time())}"
    
    # Initialize the status as 'PENDING' in our store
    payment_status_store[external_ref] = {
        "status": "PENDING",
        "message": "Waiting for you to enter M-Pesa PIN...",
        "receipt": None
    }

    payload = {
        "amount": amount,
        "phone_number": phone,
        "channel_id": int(CHANNEL_ID),
        "provider": "m-pesa",
        "external_reference": external_ref,
        "customer_name": "Subscriber",
        "account_id": int(ACCOUNT_ID),
        "callback_url": f"{PUBLIC_URL}/api/payhero-callback"
    }

    response = requests.post(PAYHERO_API_URL, json=payload, headers=headers)

    if response.status_code == 201:
        return jsonify({
            "success": True, 
            "reference": external_ref
        }), 201
    else:
        return jsonify({"success": False, "error": "Gateway connection failed. Try again."}), 400


@app.route('/api/payhero-callback', methods=['POST'])
def payhero_webhook():
    data = request.json
    response_data = data.get('response', {})
    
    status = response_data.get('Status')
    external_ref = response_data.get('ExternalReference')
    result_desc = response_data.get('ResultDesc', 'No description')
    receipt = response_data.get('MpesaReceiptNumber', 'N/A')
    
    print("\n" + "="*60)
    print(f"CALLBACK RECEIVED FOR: {external_ref}")
    print(f"Real Status: {status}")
    print(f"Result: {result_desc}")
    print("="*60 + "\n")

    # UPDATE THE STORE WITH THE REAL RESULT
    if external_ref in payment_status_store:
        payment_status_store[external_ref]["status"] = status
        payment_status_store[external_ref]["message"] = result_desc
        payment_status_store[external_ref]["receipt"] = receipt

    return jsonify({"status": "received"}), 200


# ==========================================
# NEW ROUTE: FOR THE FRONTEND TO POLL
# ==========================================
@app.route('/api/check-status', methods=['POST'])
def check_status():
    data = request.json
    ref = data.get('reference')
    
    if ref in payment_status_store:
        return jsonify(payment_status_store[ref])
    else:
        return jsonify({"status": "UNKNOWN", "message": "Transaction ID not found"}), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)