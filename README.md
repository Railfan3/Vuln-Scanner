🛡️ ScanForge - Vulnerability Scanner
ScanForge is a lightweight, modular vulnerability scanner developed in Python. It allows cybersecurity professionals, students, and system administrators to quickly identify common vulnerabilities across networks, web applications, and local systems. The tool is designed with simplicity, extensibility, and efficiency in mind.

🔍 Features
✅ Port Scanning – Identifies open TCP ports and associated services

🌐 Web Vulnerability Detection – Detects common issues like:

SQL Injection

XSS (Cross-Site Scripting)

Directory Listing

Unsecured Headers

🔗 URL Scanner – Crawls and checks for weak URLs and misconfigurations

🔑 Admin Panel Finder – Locates possible admin panel endpoints on websites

🖥️ System Scanner – Flags outdated packages and weak configurations

📄 Report Generation – Outputs findings in a structured format (TXT/HTML/JSON)

🧩 Modular Design – Easily add new scanning modules or plugins

🛠️ Tech Stack
Language: Python 3

Libraries Used:

requests

socket

threading

bs4 (BeautifulSoup)

colorama

argparse

json, os, re

🚀 Getting Started
📥 Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/scanforge.git
cd scanforge
▶️ Run the Scanner
bash
Copy
Edit
python scanforge.py --target https://example.com
🛠️ Available Options
bash
Copy
Edit
--target     URL or IP to scan
--scan       Type of scan: [port, web, admin, system, full]
--report     Generate report: [txt, html, json]
📦 Output Example
text
Copy
Edit
Target: https://example.com

[+] Port 80 open - HTTP
[+] Found SQLi vulnerability at /product?id=12
[+] Missing security headers: X-Frame-Options, Content-Security-Policy
[+] Directory listing enabled at /uploads/
💡 Use Cases
🔐 Ethical hacking & penetration testing

🧪 Security labs or Capture The Flag (CTF) challenges

🏫 Educational tool for cybersecurity students

🏢 Internal audits for small businesses


🔮 Future Enhancements
🌍 Web GUI version using Flask or React

📦 Plugin marketplace for community-based modules

🧠 AI-assisted vulnerability detection (ML models)

🔁 Automated scan scheduling and webhook alerts

🧑‍💻 Author
Mukul Chouhan
🎓 Electronics and Communication Engineering | Security Enthusiast

🌐 [https://www.linkedin.com/in/mukul-chouhan-596291295/] 

📄 License
This project is licensed under the MIT License.
See the LICENSE file for more details.
