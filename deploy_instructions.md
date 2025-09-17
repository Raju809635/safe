# SafeMate Care - Web Deployment Guide

## Files Created:
- `app.py` - Flask web application
- `templates/index.html` - Web interface with MediaPipe gesture detection
- `requirements_web.txt` - Web dependencies
- `Procfile` - Heroku deployment config
- `runtime.txt` - Python version

## Deployment Options:

### 1. Heroku (Recommended)
```bash
# Install Heroku CLI, then:
heroku create safemate-care
git add .
git commit -m "Web version"
git push heroku main
```

### 2. Railway
```bash
# Connect GitHub repo to Railway
# Auto-deploys from main branch
```

### 3. Render
```bash
# Connect GitHub repo to Render
# Uses Procfile automatically
```

## Local Testing:
```bash
pip install -r requirements_web.txt
python app.py
# Visit: http://localhost:5000
```

## Features:
✅ Web-based gesture detection (MediaPipe Web)
✅ Firebase cloud storage
✅ Location detection
✅ Manual SOS button
✅ Mobile-friendly interface

## Note:
- Firebase key must be uploaded securely to deployment platform
- WhatsApp integration removed (requires business API for web)
- Sound alerts replaced with browser notifications