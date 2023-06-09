import csv
from datetime import datetime

from .settings import DATE_FORMAT


def save_to_csv(name, data, path):
    now = datetime.now()
    now_formatted = now.strftime(DATE_FORMAT)
    file_name = f'{name}_{now_formatted}.csv'
    file_path = path / file_name
    with open(file_path, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, dialect='unix')
        writer.writerows(data)
