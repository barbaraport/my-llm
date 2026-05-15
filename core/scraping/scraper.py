from bs4 import BeautifulSoup
import requests


class Scraper():
    @staticmethod
    def _get_static_website_content(url: str) -> BeautifulSoup:
        response = requests.get(url)
        response.raise_for_status()

        return BeautifulSoup(response.text, "lxml")
    
    @staticmethod
    def find_in_page(page: str, tag: str, attribute: str, value: str) -> str:
        website_content = Scraper._get_static_website_content(page)
        element = website_content.find(tag, attrs={attribute: value})

        if element is None: return ""
        
        return element.get_text(separator=" ", strip=True)