from bs4 import BeautifulSoup
import requests


class Scraper():
    @staticmethod
    def get_static_website_content(url: str) -> str:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")
        return soup.get_text()