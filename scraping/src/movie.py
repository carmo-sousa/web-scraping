"""
Faz um scraping no url http://www.adorocinema.com/filmes/todos-filmes/notas-espectadores/
e retorna uma lista com os melhores filmes de todos os tempos
"""
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import re


def movies(url):
    pattern = r"\s{2,}"
    get = requests.get(url).text
    soup = BeautifulSoup(get, "html.parser")
    div_movies = soup.find_all("li", class_="mdl")

    movies = []

    for movie in div_movies:
        title = movie.find("a", class_="meta-title-link").text.strip()
        time = movie.find("div", class_="meta-body-item meta-body-info").text.strip()
        print(re.sub("\s{2,}|/", " ", time).replace("\n", "/"))
        # movies.append((title, date, time))

    return movies
