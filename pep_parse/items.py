import scrapy


class PepParseItem(scrapy.Item):
    """PEP parsing item"""
    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
