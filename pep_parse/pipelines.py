from collections import defaultdict

from scrapy import Spider

from pep_parse.utils import save_to_csv

from .settings import BASE_DIR, RESULTS_FOLDER


class PepParsePipeline:
    """Pipeline to collect PEP parsing statistics"""

    def __init__(self):
        self.pep_stats = defaultdict(int)

    def open_spider(self, spider):
        result_dir = BASE_DIR / RESULTS_FOLDER
        result_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        self.pep_stats[item['status']] += 1
        return item

    def close_spider(self, spider):
        self.pep_stats['Total'] = sum(self.pep_stats.values())
        data = [('Статус', 'Колличество'), *self.pep_stats.items()]
        save_to_csv('status_summary', data, BASE_DIR / RESULTS_FOLDER)
