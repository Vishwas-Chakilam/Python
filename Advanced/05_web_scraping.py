# 05_web_scraping.py

# This script demonstrates basic web scraping using the requests and BeautifulSoup libraries.

import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    """Fetch the HTML content from a URL."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.text

def parse_html(html):
    """Parse the HTML content and extract titles of articles."""
    soup = BeautifulSoup(html, 'html.parser')
    titles = [title.get_text() for title in soup.find_all('h2')]
    return titles

def main():
    url = 'https://example.com/'  # Replace with a real URL
    html = fetch_html(url)
    titles = parse_html(html)
    
    print("Article titles:")
    for title in titles:
        print(title)

if __name__ == "__main__":
    main()
