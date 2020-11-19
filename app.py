"""
Web scraping
Script que faz uma requisição para uma determinada URL
E envia um email com uma lista de filmes
"""

import os

from dotenv import load_dotenv

from src.email import mail
from src.filme import movies
from src.html import html

load_dotenv()


def app():
    URL = os.getenv("URL")

    print("⚙ Pegando os filmes...")
    get_movies = movies(URL)

    print("⚙ Montando o HTML...")
    mount_html = html(get_movies)

    print("⚙ Enviando o e-mail...")
    mail(mount_html)
    print("✔ E-mail enviado!")


if __name__ == "__main__":
    app()