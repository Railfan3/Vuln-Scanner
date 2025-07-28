import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from .payloads import get_payloads

def scan_url(url, vuln_type="xss"):
    result = []
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        forms = soup.find_all("form")

        for form in forms:
            action = form.get("action") or url
            method = form.get("method", "get").lower()
            inputs = form.find_all(["input", "textarea"])
            target_url = urljoin(url, action)  # Correct URL joining

            # 🔍 CSRF Detection
            if vuln_type == "csrf":
                has_token = any("csrf" in (inp.get("name") or "").lower() for inp in inputs)
                if not has_token and method == "post":
                    result.append({
                        "url": target_url,
                        "type": "CSRF",
                        "evidence": "Missing CSRF token in POST form"
                    })
                continue  # Skip payload testing for CSRF

            for payload in get_payloads(vuln_type):
                data = {}
                for inp in inputs:
                    name = inp.get("name")
                    if name:
                        data[name] = payload

                try:
                    if method == "post":
                        response = requests.post(target_url, data=data, timeout=10)
                    else:
                        response = requests.get(target_url, params=data, timeout=10)

                    # Detection logic
                    if vuln_type == "xss" and payload in response.text:
                        result.append({
                            "url": target_url,
                            "payload": payload,
                            "type": "XSS",
                            "evidence": payload
                        })
                    elif vuln_type == "sqli" and re.search(r"sql|mysql|syntax|error|warning", response.text, re.IGNORECASE):
                        result.append({
                            "url": target_url,
                            "payload": payload,
                            "type": "SQLi",
                            "evidence": response.text[:200]
                        })
                    elif vuln_type == "cmdi" and re.search(r"(uid=|root|/etc/passwd|user|bin)", response.text, re.IGNORECASE):
                        result.append({
                            "url": target_url,
                            "payload": payload,
                            "type": "CMDi",
                            "evidence": response.text[:200]
                        })

                except requests.exceptions.RequestException as e:
                    print(f"Request error: {e}")
    except Exception as e:
        print(f"Scan failed for {url}: {e}")
    return result
