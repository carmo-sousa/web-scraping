"""
Web scraping
Script que faz uma requisição para uma determinada URL
E envia um email com uma lista de filmes
"""

import os

from dotenv import load_dotenv
from apscheduler.schedulers.blocking import BlockingScheduler

from src.email import mail
from src.movie import movies
from src.html import html

load_dotenv()


def app():
    USER = os.getenv("MAIL_FROM")
    PASSWORD = os.getenv("PASSWORD")
    TO = os.getenv("MAIL_TO")
    URL = os.getenv("URL")

    print("⚙ Pegando os filmes...")
    get_movies = movies(URL)

    print("⚙ Montando o HTML...")
    mount_html = html(get_movies)

    print("⚙ Enviando o e-mail...")
    mail(mount_html, USER, PASSWORD, TO)
    print("✔ E-mail enviado!")

app()

# sched = BlockingScheduler()

# @sched.scheduled_job('interval', minutes=1)
# def start():
#     app()

# sched.start()
