import re

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """PEP parsing spider"""
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_links = response.xpath(
            "//table[contains(@class, 'pep')]//tr//td//a/@href")
        for pep_link in pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_title = response.css('h1.page-title::text').get()
        status = response.css(
            'dl dt:contains("Status")+dd abbr::text').get()
        matches = re.search(r'PEP (\d+) – (.+)', pep_title)
        if matches:
            yield PepParseItem(number=matches.group(1),
                               name=matches.group(2),
                               status=status)
