<<<<<<< HEAD
# 🏥 SafeMate Care

> **AI-powered Emergency SOS System for Healthcare & Elderly Assistance using Gesture Recognition + Cloud**

SafeMate Care empowers **elderly patients, disabled individuals, or hospitalized patients** to raise instant SOS alerts **using hand gestures (like a closed fist)**. The alert sends real-time location and room number to **family members, caretakers, or hospital staff**, enabling **faster emergency responses**.

---

## 📌 Features

| Feature                      | Description                                                            |
|------------------------------|-----------------------------------------------------------------------|
| ✋ **Gesture-triggered SOS**    | Show *fist* gesture to webcam to raise an emergency alert                |
| 📸 **Photo Capture**            | Captures real-time image for verification                               |
| 🌍 **Location Detection**       | Finds approximate location (city/state + lat/lng) via IP                |
| 🏥 **Room Number Tracking**     | Includes **hospital Room/Ward number** in every SOS alert              |
| ☁ **Firebase Integration**      | Stores SOS alerts securely in Firebase Realtime Database                |
| 📲 **WhatsApp Notification**    | Sends formatted SOS message with location & room to caretakers         |
| 📢 **Sound Alarm**              | Plays local loud alarm to alert nearby medical staff or caregivers     |

---

## ⚙️ Tech Stack

| Module                 | Technology                       |
|------------------------|----------------------------------|
| **Gesture Detection**  | MediaPipe + OpenCV               |
| **Cloud Database**     | Firebase Realtime Database       |
| **Location Detection** | Geocoder (IP-based geo lookup)   |
| **WhatsApp Integration** | pywhatkit (requires WhatsApp Web) |
| **Sound Playback**     | pygame (MP3 audio alarm)         |

---

## 🚀 How It Works
1. **Run the application → Patient shows a *fist* gesture to the webcam.**
2. 📸 **Image Captured** → Photo of the room is taken for verification.
3. 🌍 **Location Captured** → City, State, and Coordinates fetched via IP.
4. 🏥 **Room Number Included** → SOS message includes hospital Room/Ward number.
5. ☁ **Cloud Upload** → Data securely stored in Firebase under `sos_alerts/`.
6. 📲 **WhatsApp Sent** → Emergency alert sent to caregivers or hospital emergency contacts.
7. 📢 **Sound Alarm** → Loud alert sound plays in the patient’s room for immediate attention.

---

## 📂 Folder Structure

=======
# safemate
Safe Project  This repository contains the source code for the Safe project. It includes application logic, configuration files, and supporting scripts. Sensitive files such as Firebase credentials are excluded from version control for security reasons.  Please refer to the README for setup instructions and further documentation.
>>>>>>> ae7883e61d11e93a2ed8576d47fc3e07ca419d2b
