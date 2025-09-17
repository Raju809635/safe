from flask import Flask, render_template, request, jsonify
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime
import geocoder
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client

app = Flask(__name__)

# Emergency contact details
EMERGENCY_EMAIL = "rbomma074@gmail.com"
EMERGENCY_PHONE = "+916304679550"
ROOM_NUMBER = "220"

# Email configuration (Gmail example)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USER = "rbomma074@gmail.com"
EMAIL_PASS = "geig qkep erjo axvv"

# Twilio configuration (optional)
TWILIO_SID = "your-twilio-sid"       # Change this
TWILIO_TOKEN = "your-twilio-token"   # Change this
TWILIO_PHONE = "+1234567890"         # Change this

# Initialize Firebase (optional)
try:
    if not firebase_admin._apps:
        cred = credentials.Certificate("firebase_key.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://sample-firebase-ai-app-bb474-default-rtdb.asia-southeast1.firebasedatabase.app/'
        })
    firebase_enabled = True
except FileNotFoundError:
    print("Firebase key not found - running without cloud storage")
    firebase_enabled = False

@app.route('/')
def index():
    return render_template('index.html')

def send_email_alert(location):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = EMERGENCY_EMAIL
        msg['Subject'] = "EMERGENCY ALERT - SafeMate Care"
        
        body = f"""EMERGENCY ALERT - SafeMate Care

Patient requires immediate help!
Room No: {ROOM_NUMBER}
Location: {location.get('city')}, {location.get('state')}
Coordinates: {location.get('latlng')}
Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Please respond immediately!"""
        
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        text = msg.as_string()
        server.sendmail(EMAIL_USER, EMERGENCY_EMAIL, text)
        server.quit()
        print(f"Email sent successfully to {EMERGENCY_EMAIL}")
        return True
    except Exception as e:
        print(f"Email failed: {e}")
        return False

def send_sms_alert(location):
    try:
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        
        message_body = f"""
🚨 EMERGENCY - SafeMate Care
🏥 Room {ROOM_NUMBER} needs help!
📍 {location.get('city')}, {location.get('state')}
⏰ {datetime.now().strftime('%H:%M')}
        """
        
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE,
            to=EMERGENCY_PHONE
        )
        return True
    except Exception as e:
        print(f"SMS failed: {e}")
        return False

@app.route('/trigger_sos', methods=['POST'])
def trigger_sos():
    try:
        # Get location
        g = geocoder.ip('me')
        location = {
            "city": g.city,
            "state": g.state,
            "latlng": g.latlng
        }
        
        # Save to Firebase (if available)
        if firebase_enabled:
            ref = db.reference("sos_alerts")
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            data = {
                "timestamp": now,
                "room_number": ROOM_NUMBER,
                "location": location,
                "alert_type": "gesture_detected"
            }
            
            ref.push(data)
        else:
            print(f"SOS Alert: Room {ROOM_NUMBER}, Location: {location}")
        
        # Send email and SMS alerts
        print(f"Attempting to send alerts for location: {location}")
        email_sent = send_email_alert(location)
        sms_sent = send_sms_alert(location)
        print(f"Email sent: {email_sent}, SMS sent: {sms_sent}")
        
        return jsonify({
            "success": True,
            "message": "SOS alert triggered successfully",
            "location": location,
            "firebase_enabled": firebase_enabled,
            "email_sent": email_sent,
            "sms_sent": sms_sent
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))