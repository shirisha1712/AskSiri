# AI Siri Log Analyzer

AI Siri Log Analyzer is an intelligent assistant designed to simplify log analysis. Just upload your logs, ask questions naturally, and receive instant insights in a conversational style.

## Features
- Upload log files (including PDF, TXT, LOG)
- Ask questions about your logs
- Get instant AI-powered insights
- Modern, responsive UI
- User authentication (login/register)

## Requirements
- Python 3.8+
- Flask
- python-dotenv
- PyPDF2
- google-generativeai

## Installation
1. Clone this repository or upload your code to Render.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add your Gemini API key:
   ```env
   AI_API_KEY=your_gemini_api_key_here
   ```
4. Run the app locally:
   ```bash
   python app.py
   ```

## Deployment on Render
1. Push your code to a GitHub repository.
2. Go to [Render.com](https://render.com/) and create a new Web Service.
3. Connect your GitHub repo and select the root directory containing `app.py`.
4. Set the build and start commands:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
5. Add your environment variable `AI_API_KEY` in the Render dashboard.
6. Deploy!

## File Structure
```
app.py
requirements.txt
static/
    css/
    js/
    img/
templates/
    base.html
    index.html
    analyzer.html
    about.html
    contact.html
    login.html
    register.html
```

## Notes
- Make sure your `requirements.txt` includes all dependencies.
- For production, set `debug=False` in `app.py`.
- If you use a custom domain, configure it in Render settings.

---

© 2025 AI Siri Log Analyzer. All rights reserved.
