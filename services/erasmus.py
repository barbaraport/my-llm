from core.scraping.scraper import Scraper
from services.base_service import BaseService
from settings.get_setting import get_setting

class ErasmusService(BaseService):
    def summarize(self) -> str:
        url = get_setting("CATALOGUE_URL")
        website_content = Scraper.get_static_website_content(url=url)
        return self.summarizer.summarize(website_content)