"""
Web scraping
Script que faz uma requisição para uma determinada URL
E envia um email com uma lista de filmes
"""
import logging

from .settings import USER, PASSWORD, TO, URL
from .src.email import mail
from .src.movie import movies
from .src.html import html


def run():
    logging.info("⚙ Pegando os filmes...")
    get_movies = movies(URL)

    logging.info("🔧 Montando o HTML...")
    mount_html = html(get_movies)

    logging.info("✉ Enviando o e-mail...")
    mail(mount_html, USER, PASSWORD, TO)
    logging.info("✔ E-mail enviado!")
