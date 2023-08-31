import sys
import re
from helper.wiki import WikiArticle

def extract_categories(text):
    lines = text.split('\n')
    pattern = r'\[\[Category:(.*?)(?:\|.*)?\]\]'
    category_lines = [line for line in lines if re.search(pattern, line)]
    return category_lines

wiki_article = WikiArticle()
uk_text = wiki_article.get_uk_text()
print(extract_categories(uk_text))