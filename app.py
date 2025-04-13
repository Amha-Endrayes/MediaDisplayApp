import os
from datetime import datetime, timedelta
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configurations
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'media')
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'mp4'}

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Global dictionary for connected devices.
connected_devices = {}

# Global slideshow settings (delay in milliseconds and pause state).
slideshow_settings = {
    "delay": 3000,  # Default delay is 3000ms = 3 seconds.
    "paused": False
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    media_files = os.listdir(app.config['UPLOAD_FOLDER'])
    # Filter devices active within the last 5 minutes.
    threshold = datetime.now() - timedelta(minutes=5)
    active_devices = {ip: info for ip, info in connected_devices.items() if info['last_seen'] > threshold}
    return render_template('dashboard.html', media_files=media_files, devices=active_devices, slideshow_settings=slideshow_settings)

# Updated Upload Page Route to a more descriptive URL.
@app.route('/admin/upload', methods=['GET', 'POST'])
def upload_media():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('dashboard'))
    return render_template('upload.html')

@app.route('/display')
def display():
    # Log the connecting device using its IP address.
    user_ip = request.remote_addr
    connected_devices[user_ip] = {'ip': user_ip, 'last_seen': datetime.now()}
    media_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('display.html', media_files=media_files)

@app.route('/media/<filename>')
def media(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/api/media')
def api_media():
    media_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return jsonify(media_files)

@app.route('/api/settings')
def api_settings():
    return jsonify(slideshow_settings)

# Updated: Convert delay from seconds to milliseconds.
@app.route('/update_slideshow', methods=['POST'])
def update_slideshow():
    global slideshow_settings
    try:
        delay_seconds = int(request.form.get('delay', 3))
    except ValueError:
        delay_seconds = 3
    slideshow_settings['delay'] = delay_seconds * 1000  # Convert seconds to milliseconds.
    paused = request.form.get('paused') == 'on'
    slideshow_settings['paused'] = paused
    return redirect(url_for('dashboard'))

# New route to remove a media file.
@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    return redirect(url_for('dashboard'))

# New route to update/replace a media file.
@app.route('/update/<filename>', methods=['GET', 'POST'])
def update_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        if file and allowed_file(file.filename):
            if os.path.exists(file_path):
                os.remove(file_path)
            new_filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))
            return redirect(url_for('dashboard'))
    return render_template('update.html', old_filename=filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
