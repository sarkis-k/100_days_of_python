from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_page = response.text

soup = BeautifulSoup(yc_page, "html.parser")
title = soup.title

articles = soup.find_all(name="a", class_="titlelink")
articles_texts = []
articles_links = []
for article_tag in articles:
    articles_texts.append(article_tag.getText())
    articles_links.append(article_tag.get("href"))
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

index = article_upvotes.index(max(article_upvotes))
print(articles_texts[index]+articles_links[index])




