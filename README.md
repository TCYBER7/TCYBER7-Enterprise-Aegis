# ⚡ TCYBER7 Enterprise Aegis (Anti-AI & Bot Interceptor)

> **Enterprise-Grade Reverse Proxy WAF & Active Threat Neutralizer**
> Developed by **TCYBER7**

![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)
![License MIT](https://img.shields.io/badge/license-MIT-green.svg)
![Dependencies](https://img.shields.io/badge/dependencies-Zero%20(Pure%20Python)-red.svg)
![Tier](https://img.shields.io/badge/edition-Enterprise%20B2B-black.svg)

Stop AI scrapers, vulnerability scanners, and automated exploit bots *before* they even touch your internal backend infrastructure. 

**TCYBER7 Enterprise Aegis** acts as an active frontline defense layer. Traditional Web Application Firewalls (WAFs) return standard `403 Forbidden` errors (which train adaptive AI bots to refine their attack payloads). Aegis operates differently: it executes **Silent TCP Drops (Tarpitting)**, causing automated bot connections to hang, timeout, and terminate abruptly without receiving any HTTP response headers.

---

## 🛡️ Core Features

* 🛑 **Silent TCP Drop Engine:** Kills automated connections raw at the socket level without sending HTTP headers, freezing scanner algorithms.
* 🤖 **Anti-AI Signatures:** Instantly blocks GPTBot, ClaudeBot, Bytespider, headless browser frameworks (Puppeteer, Selenium, Headless Chrome), and scanning tools (Nmap, ZGrab, Masscan).
* 🪤 **Lethal Honeypot Traps:** Automatically blacklists IP addresses permanently upon detecting attempts to scan sensitive paths (e.g., `/.env`, `/wp-admin`, `/.git/`, `/config.php`).
* 🚀 **1-Click Deployment:** The Enterprise package includes an automated Bash payload dropper (`deploy_aegis.sh`) that installs the core engine to `/opt/tcyber7/` and sets up a persistent `systemd` background service with auto-recovery on boot.
* 📦 **Zero External Dependencies:** Runs purely on Python's standard libraries. No `pip install`, zero third-party vulnerability risks, zero bloat.

---

## 💻 Safe Demo Mode (Local Testing)

You can test the core interception logic locally on Windows, macOS, or Linux without root privileges or a real backend server. The included `TCYBER7_Aegis_Demo.py` runs on port `8888` and simulates a dummy backend.

### 1. Run the Demo Script
```bash
python3 TCYBER7_Aegis_Demo.py
(Use python if you are on Windows)

2. Test Clean Traffic
Open your web browser and navigate to:
http://127.0.0.1:8888

(You will see a green "Welcome" message confirming clean traffic access)

3. Test Bot Interception
Open a new terminal window and simulate a bot request using curl:

curl http://127.0.0.1:8888 http://127.0.0.1:8888
Result: Aegis will log [THREAT NEUTRALIZED], instantly drop the socket connection, and flag your IP address.

4. Test Honeypot Trap
In your browser, attempt to access a trap path:
http://127.0.0.1:8888/wp-admin

Result: The browser will hang infinitely (Tarpit effect), and your IP will be blacklisted for the session.

🛒 Purchase The Full Enterprise Package
The full Enterprise Edition ($150+) contains the 1-Click production installer (deploy_aegis.sh) for live Linux servers, complete Systemd service integration, and automated reverse proxy forwarding to your internal server ports (e.g., port 8080).

👉 Purchase Enterprise Aegis on Gumroad(https://https://tcyber7.gumroad.com/l/gekdiv)
📄 License
This repository contains the public demo code. The full enterprise deployment bundle is distributed under the MIT License for commercial license holders.
