# Secure File Sharing System

[![Python](https://img.shields.io/badge/Language-Python_3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.org/)
[![AES-256](https://img.shields.io/badge/Cryptography-AES--256--CFB-red?style=for-the-badge&logo=shield)](https://pycryptodome.readthedocs.io/)
[![Bootstrap](https://img.shields.io/badge/Frontend-Bootstrap_5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

A web application built with Flask and PyCryptodome that provides authenticated, symmetric file encryption (AES-256-CFB) for secure file storage and on-the-fly decryption upon download with automated temporary file cleanup.

---

## Project Overview

* **The Problem:** Unencrypted file uploads stored on server drives are vulnerable to unauthorized access and data breaches if the underlying host or storage bucket is compromised.
* **The Solution:** Encrypts files at the byte level during the upload stream using AES-256 in CFB mode before writing to disk, and securely handles decryption upon request with short-lived temporary file lifecycle management.

### Key Features
* **AES-256-CFB Encryption:** Generates a unique 16-byte Initialization Vector (IV) for every file upload to prevent replay attacks and pattern analysis.
* **Environment Key Isolation:** Reads the 256-bit symmetric key securely from environment variables (`.env`).
* **Automated Lifecycle Cleanup:** Purges temporary decrypted files from the buffer directory after 60 seconds to minimize exposure windows on disk.
* **Responsive Bootstrap UI:** Offers clean file selection, upload forms, and immediate download/decrypt triggers.

---

## Tools & Technologies Used

| Category | Technology |
| :--- | :--- |
| **Backend Framework** | Python / Flask |
| **Cryptography Library** | PyCryptodome |
| **Frontend UI** | HTML5 / Jinja2 / Bootstrap 5 |

---

## Proof of Work

Demonstration of local environment setup, file upload/encryption pipeline, `.enc` file storage verification and on-the-fly download decryption.

<video src="https://github.com/user-attachments/assets/4f08fb73-918e-415b-bf29-54c0a283436e" controls="controls" muted="muted" style="max-height:640px; width:100%;">
</video>

---
