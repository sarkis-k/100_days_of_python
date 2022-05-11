from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_page = response.text


soup = BeautifulSoup(movies_page, "html.parser")
title = soup.title

movies_list = [text.getText() for text in soup.find_all(name="h3", class_="title")]
movies_list.reverse()
print(movies_list)

with open("movies.txt", "a") as file:
    for movie in movies_list:
        file.write(movie+"\n")





