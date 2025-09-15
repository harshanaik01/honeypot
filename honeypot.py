import socket
import logging
from datetime import datetime
from threading import Thread
from database import init_db, log_attack
from alert import send_email_alert

logging.basicConfig(filename="honeypot.log", level=logging.INFO)

# Initialize database
init_db()

# Fake service banners
BANNERS = {
    22: b"SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5\r\n",
    21: b"220 (vsFTPd 3.0.3)\r\n",
    80: b"HTTP/1.1 200 OK\r\nServer: Apache/2.4.41 (Ubuntu)\r\n\r\n<html><h1>Fake Web Server</h1></html>"
}

def handle_client(conn, addr, port):
    ip = addr[0]
    try:
        # Send fake banner
        if port in BANNERS:
            conn.send(BANNERS[port])
        
        data = conn.recv(1024).decode("utf-8", errors="ignore")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        logging.info(f"[{timestamp}] Connection from {ip}:{port} -> {data}")
        log_attack(ip, port, data, timestamp)

        # Send email alert
        send_email_alert(ip, port, data)

    except Exception as e:
        logging.error(f"Error: {e}")
    finally:
        conn.close()

def start_honeypot(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("0.0.0.0", port))
    sock.listen(5)
    print(f"[+] Honeypot listening on port {port}")

    while True:
        conn, addr = sock.accept()
        thread = Thread(target=handle_client, args=(conn, addr, port))
        thread.start()

if __name__ == "__main__":
    ports = [22, 21, 80]  # Fake SSH, FTP, HTTP
    for port in ports:
        t = Thread(target=start_honeypot, args=(port,))
        t.start()
