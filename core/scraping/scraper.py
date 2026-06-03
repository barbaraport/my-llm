from bs4 import BeautifulSoup
import requests
import asyncio


class Scraper():
    @staticmethod
    async def _get_static_website_content(url: str) -> BeautifulSoup:
        """fetches the content of a static website and returns it as a BeautifulSoup object"""
        def _sync_get(u: str):
            """synchronous function to perform the GET request, to be run in a separate thread, since requests is blocking"""
            resp = requests.get(u, timeout=(5, 30))
            resp.raise_for_status()
            return resp.text

        text = await asyncio.to_thread(_sync_get, url)
        return BeautifulSoup(text, "lxml")

    @staticmethod
    async def find_first_in_page(page: str, tag: str, attribute: str, value: str) -> str:
        """finds the first element matching the criteria in the given page and returns its text"""
        website_content = await Scraper._get_static_website_content(page)
        element = website_content.find(tag, attrs={attribute: value})

        if element is None:
            return ""

        return element.get_text(separator=" ", strip=True)

    @staticmethod
    async def find_all_by_selector(page: str, value: str) -> list[str]:
        """finds all elements matching the CSS selector in the given page and returns their text"""
        website_content = await Scraper._get_static_website_content(page)
        element = website_content.select(value)

        return [e.get_text(separator=" ", strip=True) for e in element]