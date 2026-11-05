"""
===========================================================================
 ⚡ TCYBER7 ENTERPRISE AEGIS - SAFE DEMO VERSION ⚡
===========================================================================
 Author: TCYBER7
 Target: Local Testing (Windows / macOS / Linux / Termux)
 Note: This is a standalone demo. It runs on port 8888 without root,
       and simulates a dummy backend server for safe testing.
===========================================================================
"""

import socket
import threading
import re
import logging

# ==========================================
# ⚙️ DEMO CONFIGURATION (SAFE MODE)
# ==========================================
LISTEN_HOST = '127.0.0.1'  # Runs on localhost for safety
LISTEN_PORT = 8888         # Non-privileged port (no root required)
BANNED_IPS = set()

# 🤖 AI & BOT SIGNATURES (Regex)
AI_BOT_SIGNATURES = re.compile(
    r'(GPTBot|ChatGPT|Anthropic|ClaudeBot|Bytespider|CCBot|'
    r'python-requests|urllib|curl|wget|HeadlessChrome|Puppeteer|'
    r'Selenium|Scrapy|Nmap|ZGrab|Masscan)', re.IGNORECASE
)

# 🪤 HONEYPOT PATHS (Lethal Traps)
LETHAL_TRAPS = ['/wp-admin', '/.env', '/config.php', '/admin/', '/phpmyadmin', '/.git/']

# Enterprise Logging Configuration
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s | %(levelname)s | %(message)s', 
    datefmt='%H:%M:%S'
)

def drop_connection(client_socket, ip, reason):
    """Silently drops the TCP connection, causing bot timeouts (Tarpit effect)."""
    logging.warning(f"🚨 [THREAT NEUTRALIZED] IP: {ip} | Reason: {reason}")
    BANNED_IPS.add(ip)
    try:
        # Close socket without sending any HTTP response
        client_socket.close()
    except: pass

def handle_client(client_socket, address):
    ip = address[0]
    
    # 1. Check if IP is already blacklisted
    if ip in BANNED_IPS:
        logging.error(f"❌ [BLOCKED] Banned IP attempting access: {ip} -> Auto-Drop!")
        client_socket.close()
        return

    try:
        request = client_socket.recv(4096).decode('utf-8', errors='ignore')
        if not request:
            return client_socket.close()

        headers = request.split('\r\n')
        try:
            method, path, protocol = headers[0].split(' ')
        except ValueError:
            return drop_connection(client_socket, ip, "Malformed HTTP Request")

        # 2. Check Honeypot Traps
        if any(trap in path for trap in LETHAL_TRAPS):
            return drop_connection(client_socket, ip, f"Honeypot Triggered on {path}")

        # 3. Check AI & Bot Signatures
        user_agent = ""
        for header in headers:
            if header.lower().startswith('user-agent:'):
                user_agent = header.split(':', 1)[1].strip()
                break
        
        if not user_agent or AI_BOT_SIGNATURES.search(user_agent):
            return drop_connection(client_socket, ip, f"AI/Bot Signature: {user_agent}")

        # ==========================================
        # ✅ IF CLEAN: SIMULATE ENTERPRISE BACKEND
        # ==========================================
        logging.info(f"✅ [CLEAN TRAFFIC] IP: {ip} -> Access Granted ({path})")
        
        # Dummy backend response
        safe_response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            "Connection: close\r\n\r\n"
            "<html><body style='background:#0a0a0a; color:#00ff00; font-family:monospace; text-align:center; margin-top:100px;'>"
            "<h1>🛡️ WELCOME TO THE PROTECTED ENTERPRISE SERVER!</h1>"
            "<p>Your traffic was deemed clean by TCYBER7 Aegis.</p>"
            "<p>[DEMO ENVIRONMENT]</p>"
            "</body></html>"
        )
        client_socket.sendall(safe_response.encode('utf-8'))
        
    except Exception as e:
        pass
    finally:
        client_socket.close()

def start_demo():
    print(r"""
     ___________.__                                
    \__    ___/|  |__   ____   _____  ______  ______
      |    |   |  |  \_/ __ \ /     \ \____ \/  ___/
      |    |   |   Y  \  ___/|  Y Y  \|  |_> >___ \ 
      |____|   |___|  /\___  >__|_|  /|   __/____  >
                    \/     \/      \/ |__|       \/ 
    ==================================================
    [+] TCYBER7 AEGIS - SAFE DEMO MODE ACTIVE
    [+] SIMULATED BACKEND RUNNING ON PORT {}
    ==================================================
    """.format(LISTEN_PORT))
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((LISTEN_HOST, LISTEN_PORT))
    server.listen(100)

    try:
        while True:
            client_socket, address = server.accept()
            threading.Thread(target=handle_client, args=(client_socket, address), daemon=True).start()
    except KeyboardInterrupt:
        print("\n[!] Shutting down Aegis Demo...")
        server.close()

if __name__ == '__main__':
    start_demo()