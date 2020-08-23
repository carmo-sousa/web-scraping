#!/bin/python3
"""
Web scraping
Script que faz uma requisição para uma determinada URL
E envia um email com uma lista de filmes
"""
import email.message
import smtplib

import requests

import config  # Arquivo com senhas e emails.
from bs4 import BeautifulSoup
from constantes import TEMPLATE, URL


def get_filmes(url: str) -> list:
    """
    Faz a requisição e devolve uma lista de tuplas onde cada item da tupla é o
    título, ano de lançamento e duração respectivamente.
    E retorna uma lista onde cada indice é uma tupla representando um filme.
    """

    # Faz a requisição e retorna o texto HTML
    get = requests.get(url).text
    # print(get)

    # Cria uma instancia de BeautifulSoup passando a variavel get no
    # primeiro parametro e no segundo parametro é passado o tipo de arquivo
    soup = BeautifulSoup(get, 'html.parser')

    # Filtra a div com a lista dos filmes
    lista_de_filmes = soup.find_all('div', class_='data_box')

    filmes: list = []

    # Filtra o título, ano de lançamento e a duração do filme
    # Cria uma tupla com os dados e adiciona na variavel filmes
    for filme in lista_de_filmes:
        title = filme.find('h2').text.strip()
        lancamento, duracao = filme.find(
            'div', class_='oflow_a').text.strip().split('\n')
        filmes.append((title, lancamento, duracao))

    return filmes


def monta_template(list_filmes: list) -> str:
    """Monta o template html com a lista dos filmes"""
    template_lista: str = ''

    for filme in list_filmes:
        template_lista += (
            "<tr>\n<td>{0}</td>\n<td>{1}</td>\n<td>{2}</td>\n</tr>"
            .format(filme[0], filme[1], filme[2])
        )

    # Troca o data_list pela lista dos filmes
    return TEMPLATE.replace('data_list', template_lista)


def envia_email(mensagem: str) -> None:
    """Responsável por enviar o e-mail"""
    password = config.PASSWORD

    msg = email.message.Message()
    msg['From'] = config.EMAIL_FROM
    msg['To'] = config.EMAIL_TO
    msg['Subject'] = 'Lista de filmes'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(mensagem)

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

    print(f'Successfully sent email to {msg["To"]}')


filmes: list = get_filmes(URL)
template: str = monta_template(filmes)
print(template)

envia_email(template)
