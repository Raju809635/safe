from flask import Flask, render_template, request, jsonify
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime
import geocoder
import os

app = Flask(__name__)

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
                "room_number": "220",
                "location": location,
                "alert_type": "gesture_detected"
            }
            
            ref.push(data)
        else:
            print(f"SOS Alert: Room 220, Location: {location}")
        
        return jsonify({
            "success": True,
            "message": "SOS alert triggered successfully",
            "location": location,
            "firebase_enabled": firebase_enabled
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))