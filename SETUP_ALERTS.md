# 📧📱 Setup Email & SMS Alerts

## Email Setup (Gmail):
1. **Enable 2-Factor Authentication** on Gmail
2. **Generate App Password:**
   - Gmail → Settings → Security → 2-Step Verification → App passwords
   - Generate password for "SafeMate Care"
3. **Update in app.py:**
   ```python
   EMAIL_USER = "your-gmail@gmail.com"
   EMAIL_PASS = "your-16-digit-app-password"
   EMERGENCY_EMAIL = "caregiver@example.com"
   ```

## SMS Setup (Twilio):
1. **Sign up at twilio.com** (free trial)
2. **Get credentials:**
   - Account SID
   - Auth Token  
   - Twilio phone number
3. **Update in app.py:**
   ```python
   TWILIO_SID = "your-account-sid"
   TWILIO_TOKEN = "your-auth-token"
   TWILIO_PHONE = "+1234567890"  # Twilio number
   EMERGENCY_PHONE = "+916304679550"  # Your number
   ```

## Environment Variables (Secure):
In Render dashboard → Environment:
```
EMAIL_USER=your-gmail@gmail.com
EMAIL_PASS=your-app-password
EMERGENCY_EMAIL=caregiver@example.com
TWILIO_SID=your-sid
TWILIO_TOKEN=your-token
TWILIO_PHONE=+1234567890
EMERGENCY_PHONE=+916304679550
```

## Test:
- Show fist gesture → Email + SMS sent automatically!