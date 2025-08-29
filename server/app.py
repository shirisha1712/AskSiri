import os
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import google.generativeai as genai # New import for Gemini
import PyPDF2

# Load API key from .env file
load_dotenv()

# The Flask app instance
app = Flask(__name__)

# Configure the Gemini API with your key
genai.configure(api_key=os.getenv("AI_API_KEY"))


# Route to serve the main HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route for AI Log Analyzer chat page
@app.route('/analyzer')
def analyzer():
    return render_template('analyzer.html')

# Route for About page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Dummy login logic (to be replaced with real authentication)
        return render_template('analyzer.html')
    return render_template('login.html')

# Route for Register page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Dummy register logic (to be replaced with real registration)
        return render_template('login.html')
    return render_template('register.html')

# Route for the AI API
@app.route('/api/analyze', methods=['POST'])
def analyze_logs():
    prompt = request.form.get('prompt', '')
    log_text = request.form.get('log_text', '')
    log_files = request.files.getlist('log_files')

    all_logs = [log_text]
    for file in log_files:
        filename = secure_filename(file.filename)
        if filename.lower().endswith('.pdf'):
            try:
                file.stream.seek(0)  # Ensure pointer is at start
                pdf_reader = PyPDF2.PdfReader(file.stream)
                pdf_text = ""
                for page in pdf_reader.pages:
                    pdf_text += page.extract_text() or ""
                file_content = pdf_text
            except Exception as e:
                file_content = f"[Error reading PDF: {e}]"
        else:
            try:
                file_content = file.read().decode('utf-8', errors='ignore')
            except Exception as e:
                file_content = f"[Error reading file: {e}]"
        all_logs.append(f"\n--- Log File: {filename} ---\n{file_content}\n")

    full_log_content = "\n".join(all_logs)
    
    ai_prompt_text = f"User Request: {prompt}\n\nLog Data:\n{full_log_content}"
    
    try:
        # --- Gemini API CALL ---
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(ai_prompt_text)
        result = response.text
        # --- END Gemini API CALL ---
        
        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)