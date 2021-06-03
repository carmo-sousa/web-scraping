"""
Web scraping
Script que faz uma requisição para uma determinada URL
E envia um email com uma lista de filmes
"""
import logging
from smtplib import SMTPAuthenticationError

from .settings import Config
from .src.email import mail
from .src.html import html
from .src.movie import movies


def run():
    try:
        logging.info("⚙ Pegando os filmes...")
        get_movies = movies(Config.URL)

        logging.info("🔧 Montando o HTML...")
        mount_html = html(get_movies)

        logging.info("✉ Enviando o e-mail...")
        # mail(mount_html, Config.USER, Config.PASSWORD, Config.TO)
        logging.info("✔ E-mail enviado!")

    except SMTPAuthenticationError as e:
        print(
            "\nNão foi possível fazer login com o email informado.",
            "\nVerifique se está autorizado o acesso de apps menos seguros.",
            "\nhttps://myaccount.google.com/lesssecureapps",
        )
