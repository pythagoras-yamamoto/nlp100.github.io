import sys
from helper.wiki import WikiArticle

wiki_article = WikiArticle()
uk_text = wiki_article.get_uk_text()
print(uk_text)