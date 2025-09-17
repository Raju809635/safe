# 🚀 Deploy SafeMate Care to Render

## Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "SafeMate Care web app"
git branch -M main
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

## Step 2: Deploy on Render
1. Go to **render.com**
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repo
4. Settings:
   - **Name:** safemate-care
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements_web.txt`
   - **Start Command:** `gunicorn app:app`

## Step 3: Add Firebase Key
1. In Render dashboard → **Environment**
2. Add environment variables or upload `firebase_key.json`

## ✅ Your app will be live at:
`https://safemate-care.onrender.com`

## Features:
- ✅ Free 750 hours/month
- ✅ HTTPS included
- ✅ Auto-deploys from GitHub
- ⚠️ Sleeps after 15min (wakes on visit)

## Test locally first:
```bash
python app.py
# Visit: http://localhost:5000
```