import sqlite3

def init_db():
    conn = sqlite3.connect("honeypot.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS attacks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  ip TEXT,
                  port INT,
                  command TEXT,
                  timestamp TEXT)''')
    conn.commit()
    conn.close()

def log_attack(ip, port, command, timestamp):
    conn = sqlite3.connect("honeypot.db")
    c = conn.cursor()
    c.execute("INSERT INTO attacks (ip, port, command, timestamp) VALUES (?, ?, ?, ?)",
              (ip, port, command, timestamp))
    conn.commit()
    conn.close()
