from asyncio import sleep
from random import uniform
import re
from typing import AsyncGenerator

from core.scraping.scraper import Scraper
from services.base_service import BaseService
from settings.get_setting import get_setting

class ErasmusService(BaseService):
    async def summarize(self) -> AsyncGenerator[str, None]:
        url = get_setting("CATALOGUE_URL")

        first_page = 1
        last_page_str = await Scraper.find_first_in_page(page=url, tag="li", attribute="class", value="ecl-pagination__item ecl-pagination__item--last")
        last_page_numbers_only = re.search(r"\d+", last_page_str)
        last_page = int(last_page_numbers_only.group()) if last_page_numbers_only else 1

        total_projects = 0
        for page in range(first_page, last_page + 1):
            wait_time = uniform(3, 7)
            await sleep(wait_time)

            projects = await Scraper.find_all_by_selector(page=url + f"?page={page}", value=".ecl-content-block.ecl-card__content-block")
            if projects != []:
                for project in projects:
                    total_projects += 1
                    website_content = f"START OF SCHOLARSHIP {total_projects}\n\n"
                    website_content += project
                    website_content += "\nEND OF SCHOLARSHIP\n\n"

                    stream =  self.summarizer.summarize(website_content)

                    async for chunk in stream:
                        yield chunk
                        
        yield "data: ###[ALL-SCHOLARSHIPS-DONE]###\n\n"