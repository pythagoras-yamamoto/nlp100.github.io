import sys
import re
from helper.wiki import WikiArticle

max_equals = 5

def extract_section_titles(text):
    all_titles = []
    
    for i in range(1, 10):
        pattern = '=' * i + r' (.*?) ' + '=' * i
        titles = re.findall(pattern, text)
        print(titles, i)
    
    return all_titles

wiki_article = WikiArticle()
uk_text = wiki_article.get_uk_text()
print( uk_text)
print(extract_section_titles(uk_text))