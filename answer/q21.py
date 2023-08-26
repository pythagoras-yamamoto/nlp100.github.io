import sys
import re
from helper.wiki import WikiArticle

def extract_categories(text):
    pattern = r'\[\[Category:(.*?)(?:\|.*)?\]\]'
    categories = re.findall(pattern, text)
    return categories

wiki_article = WikiArticle()
uk_text = wiki_article.get_uk_text()
print(extract_categories(uk_text))
