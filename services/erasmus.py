from asyncio import sleep
from random import uniform
from typing import AsyncGenerator

from core.scraping.scraper import Scraper
from services.base_service import BaseService
from settings.get_setting import get_setting

class ErasmusService(BaseService):
    async def summarize(self) -> AsyncGenerator[str, None]:
        url = get_setting("CATALOGUE_URL")

        website_content = ""
        first_page_content = Scraper.find_in_page(page=url, tag="div", attribute="class", value="ecl-content-item-block")
        website_content += first_page_content

        first_page = 1
        last_page = int(
            Scraper.find_in_page(page=url, tag="li", attribute="class", value="ecl-pagination__item ecl-pagination__item--last")
        )

        for page in range(first_page, last_page):
            wait_time = uniform(3, 7)
            await sleep(wait_time)

            website_content += Scraper.find_in_page(page=url + f"?page={page}", tag="div", attribute="class", value="ecl-content-item-block")

        stream =  self.summarizer.summarize(website_content)

        async for chunk in stream:
            yield chunk