import json
import gzip

WIKI_DATA_PATH = 'data/jawiki-country.json.gz'

class WikiArticle:
    def __init__(self, filename=WIKI_DATA_PATH):
        self.filename = filename
        self.uk_text = None

    def get_uk_text(self):
        if self.uk_text:
            return self.uk_text

        with gzip.open(self.filename, 'rt', encoding='utf-8') as f:
            for line in f:
                article = json.loads(line)
                if article['title'] == 'イギリス':
                    self.uk_text = article['text']
                    return self.uk_text