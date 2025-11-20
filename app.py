import os
import time
from flask import Flask, render_template, request, send_file, redirect, flash
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from encryption import AESCipher

# Load key from .env
load_dotenv()
AES_KEY = os.getenv("AES_KEY")

app = Flask(__name__)
app.secret_key = "secure-session-key"  # used for flash() messages

UPLOAD_FOLDER = "uploads"
DECRYPTED_TEMP = "decrypted_temp"

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DECRYPTED_TEMP, exist_ok=True)

# AES cipher instance
cipher = AESCipher(AES_KEY)


def cleanup_temp_files():
    """Delete decrypted temp files older than 60 seconds."""
    now = time.time()
    for file in os.listdir(DECRYPTED_TEMP):
        path = os.path.join(DECRYPTED_TEMP, file)
        if os.path.isfile(path) and now - os.path.getmtime(path) > 60:
            os.remove(path)


@app.route("/")
def index():
    cleanup_temp_files()
    files = os.listdir(UPLOAD_FOLDER)
    return render_template("index.html", files=files)


@app.route("/upload", methods=["POST"])
def upload():
    cleanup_temp_files()

    file = request.files.get("file")

    if not file:
        flash("No file selected.")
        return redirect("/")

    filename = secure_filename(file.filename)
    raw_data = file.read()

    # Encrypt data
    encrypted = cipher.encrypt(raw_data)

    encrypted_path = os.path.join(UPLOAD_FOLDER, filename + ".enc")
    with open(encrypted_path, "wb") as f:
        f.write(encrypted)

    flash("File encrypted and uploaded successfully!")
    return redirect("/")


@app.route("/download/<filename>")
def download(filename):
    cleanup_temp_files()

    encrypted_path = os.path.join(UPLOAD_FOLDER, filename)

    if not os.path.exists(encrypted_path):
        flash("File not found.")
        return redirect("/")

    # Decrypt file
    with open(encrypted_path, "rb") as f:
        encrypted = f.read()

    decrypted = cipher.decrypt(encrypted)
    temp_path = os.path.join(DECRYPTED_TEMP, filename.replace(".enc", ""))

    with open(temp_path, "wb") as f:
        f.write(decrypted)

    return send_file(temp_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)