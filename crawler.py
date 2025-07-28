import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

visited = set()

def crawl(url):
    urls = set()
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        for form in soup.find_all("form"):
            urls.add(url)
        for link in soup.find_all("a", href=True):
            abs_url = urljoin(url, link['href'])
            if urlparse(abs_url).netloc == urlparse(url).netloc and abs_url not in visited:
                visited.add(abs_url)
                urls.update(crawl(abs_url))
    except Exception as e:
        print(f"Error crawling {url}: {e}")
    return urls
