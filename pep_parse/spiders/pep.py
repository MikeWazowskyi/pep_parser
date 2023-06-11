import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """PEP parsing spider"""
    name = 'pep'
    pep_domain = 'peps.python.org'
    allowed_domains = [pep_domain]
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        pep_links = response.xpath(
            '//table[contains(@class, "pep")]//tr//td//a/@href')
        for pep_link in pep_links:
            pep_link = pep_link.get() + '/'
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_title = response.css('h1.page-title::text').get().strip()
        pep_title = pep_title.replace('PEP', '')
        status = response.css(
            'dl dt:contains("Status")+dd abbr::text').get()
        number, name = pep_title.split(' – ')
        yield PepParseItem(number=number,
                           name=name,
                           status=status)
