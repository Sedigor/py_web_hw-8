import json

from models import *
from connect import *


def load_data_from_json(file_name, model):
    with open(file_name, 'r', encoding='utf-8') as fd:
        data = json.load(fd)
        for item in data:
            obj = model(**item)
            obj.save()
        db_data_name = file_name.split('.')[0].title()
        print(f'{db_data_name} added to database')
        
            
if __name__ == '__main__':
    load_data_from_json('authors.json', Author)
    load_data_from_json('quotes.json', Quote)
    