
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime
import os

# Initialize Firebase only once
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_key.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://sample-firebase-ai-app-bb474-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })

def push_sos_to_cloud(location, image_name=None, room_number=None):
    """
    Pushes SOS alert data to Firebase Realtime Database.
    :param location: Dict containing city, state, latlng.
    :param image_name: (Optional) Name of the snapshot image file.
    :param room_number: (Optional) Hospital room/ward number.
    """
    ref = db.reference("sos_alerts")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = {
        "timestamp": now,
        "room_number": room_number,
        "location": {
            "city": location.get("city"),
            "state": location.get("state"),
            "latlng": location.get("latlng")
        },
        "image_uploaded": bool(image_name)
    }

    if image_name:
        data["image_path"] = os.path.abspath(image_name)

    ref.push(data)
    print("✅ SOS data pushed to Firebase")
