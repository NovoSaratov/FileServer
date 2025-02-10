from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
import os
from werkzeug.utils import secure_filename

app = Flask(__name__) # For coookie sessions"2  
app.secret_key = 'ce7a25ddeef9f03f179c4c06c8592d72e2e2d9e48a46485bf7bcefbf0d701306'
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Dummy credentials
USER_CREDENTIALS = {'admin': 'password'}

@app.route('/', methods=['GET', 'POST'])
def login():
    if 'user' in session:   
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if USER_CREDENTIALS.get(username) == password:
            session['user'] = username
            return redirect(url_for('dashboard'))
    
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('dashboard.html', files=files)

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    if 'user' not in session:
        return redirect(url_for('login'))  # Sørg for at brukeren er logget inn
    
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    return redirect(url_for('dashboard'))



@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
