from flask import Flask, render_template, request
from scanner.crawler import crawl
from scanner.scanner import scan_url
import os
from scanner.report import save_report

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        target_url = request.form.get("url")
        vuln_type = request.form.get("vuln_type")
        all_urls = crawl(target_url)
        for url in all_urls:
            results.extend(scan_url(url, vuln_type))
        save_report(results)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
