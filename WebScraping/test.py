import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import time
import random

class WebScraper:
    def __init__(self, base_url, delay=1, random_delay=True):
        self.base_url = base_url
        self.delay = delay
        self.random_delay = random_delay
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

    def fetch_page(self, url):
        """Fetch the HTML content of a page."""
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def parse_page(self, html):
        """Parse the HTML and extract data. Override this method for specific scraping logic."""
        soup = BeautifulSoup(html, 'html.parser')
        # Example: extract all paragraph texts
        data = [{'content': p.text} for p in soup.find_all('p')]
        return data

    def scrape_page(self, url):
        """Scrape a single page."""
        html = self.fetch_page(url)
        if html:
            return self.parse_page(html)
        return None

    def scrape_site(self, start_url, max_pages=10):
        """Scrape multiple pages of a site."""
        visited = set()
        to_visit = [start_url]
        all_data = []

        while to_visit and len(visited) < max_pages:
            url = to_visit.pop(0)
            if url not in visited:
                print(f"Scraping: {url}")
                visited.add(url)
                html = self.fetch_page(url)
                
                if html:
                    data = self.parse_page(html)
                    all_data.extend(data)

                    # Find more links to scrape
                    soup = BeautifulSoup(html, 'html.parser')
                    for link in soup.find_all('a', href=True):
                        next_url = urljoin(self.base_url, link['href'])
                        if next_url.startswith(self.base_url) and next_url not in visited:
                            to_visit.append(next_url)

                # Implement polite scraping with delays
                if self.random_delay:
                    time.sleep(self.delay + random.random())
                else:
                    time.sleep(self.delay)

        return all_data

    def save_to_csv(self, data, filename):
        """Save the scraped data to a CSV file using pandas."""
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False, encoding='utf-8')
        print(f"Data saved to {filename}")

# Example usage
if __name__ == "__main__":
    scraper = WebScraper("https://crawler-test.com/")
    data = scraper.scrape_site("https://crawler-test.com/", max_pages=5)
    scraper.save_to_csv(data, "scraped_data.csv")