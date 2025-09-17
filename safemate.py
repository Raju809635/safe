import cv2
import mediapipe as mp
import pygame
import pywhatkit
import geocoder
import time
from cloud_utils import push_sos_to_cloud

# --------------------- Initialization ---------------------
pygame.mixer.init()

def play_alert_sound():
    pygame.mixer.music.load("sound.mp3")
    pygame.mixer.music.play()

# Setup MediaPipe for hand detection
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
alert_triggered = False
last_alert_time = 0

# Set emergency contact number (caregiver, nurse station, or hospital emergency contact)
emergency_contact = "+919182180387"

# Set the room number (static for now, can be dynamic)
room_number = "220"

def is_fist(landmarks):
    """
    Determines if the hand is showing a closed fist.
    """
    tips_ids = [8, 12, 16, 20]
    fingers_folded = 0
    for tip in tips_ids:
        if landmarks[tip].y > landmarks[tip - 2].y:
            fingers_folded += 1
    return fingers_folded == 4

# --------------------- Main Loop ---------------------
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)
            lmList = [handLms.landmark[i] for i in range(21)]

            if is_fist(lmList) and not alert_triggered:
                if time.time() - last_alert_time > 5:
                    alert_triggered = True
                    last_alert_time = time.time()

                    # Save snapshot image
                    cv2.imwrite("sos_snapshot.jpg", img)

                    # Play SOS alert sound
                    play_alert_sound()

                    # Get approximate location
                    g = geocoder.ip('me')
                    location = {
                        "city": g.city,
                        "state": g.state,
                        "latlng": g.latlng
                    }
                    print("Location:", location)

                    # Upload to Firebase or Cloud
                    push_sos_to_cloud(location)
                    print("Emergency data pushed to cloud")

                    # Compose WhatsApp message with room number
                    message = (
                        f"🚨 *Emergency Alert - SafeMate Care*\n"
                        f"🏥 Patient requires immediate help!\n"
                        f"📍 Room No: {room_number}\n"
                        f"📌 Location: {location.get('city')}, {location.get('state')}\n"
                        f"🗺 Coords: {location.get('latlng')}"
                    )

                    try:
                        pywhatkit.sendwhatmsg_instantly(emergency_contact, message, wait_time=10, tab_close=True)
                        print("WhatsApp alert sent.")
                    except Exception as e:
                        print("WhatsApp sending failed:", e)

                    print("Healthcare SOS triggered successfully!")

            else:
                alert_triggered = False

    cv2.imshow("SafeMate Care - Raise Fist for Help", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
