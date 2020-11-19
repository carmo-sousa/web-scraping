"""
Faz um scraping no url http://www.adorocinema.com/filmes/todos-filmes/notas-espectadores/
e retorna uma lista com os melhores filmes de todos os tempos
"""
import requests
from bs4 import BeautifulSoup


def movies(url):
    get = requests.get(url).text
    soup = BeautifulSoup(get, "html.parser")
    div_movies = soup.find_all("div", class_="data_box")

    movies = []

    for filme in div_movies:
        title = filme.find("h2").text.strip()
        release, movie_time = (
            filme.find("div", class_="oflow_a").text.strip().split("\n")
        )
        movies.append((title, release, movie_time))

    return movies
