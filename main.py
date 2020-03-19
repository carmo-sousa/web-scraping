#!/bin/python3
"""
Web scraping
Script que faz uma requisição para uma determinada URL
E envia um email com uma lista de filmes
"""
import email.message
import smtplib

import requests
from bs4 import BeautifulSoup

import config

URL = "http://www.adorocinema.com/filmes/todos-filmes/notas-espectadores/"


def get_filmes(url):
    """
    Faz a requisição e devolve uma lista de tuplas onde cada item da tupla é o
    título, ano de lançamento e duração respectivamente.
    E retorna uma lista onde cada indice é uma tupla representando um filme.
    """

    # Faz a requisição e retorna o texto HTML
    get = requests.get(url).text

    # Cria uma instancia de BeautifulSoup passando a variavel get no
    # primeiro parametro e no segundo parametro é passado o tipo de arquivo
    soup = BeautifulSoup(get, 'html.parser')

    # Filtra a div com a lista dos filmes
    lista_de_filmes = soup.find_all('div', class_='data_box')

    filmes = []

    # Filtra o título, ano de lançamento e o título do filme
    # Cria uma tupla com os dados e adiciona na variavel filmes
    for filme in lista_de_filmes:
        title = filme.find('h2').text.strip()
        lancamento, duracao = filme.find('div', class_='oflow_a').text.strip().split('\n')
        filmes.append((title, lancamento, duracao))

    return filmes


def monta_msg(list_filmes):
    """Monta o template html com a lista dos filmes"""
    template_lista = ''

    for filme in list_filmes:
        template_lista += "<tr>\n<td>{0}</td>\n<td>{1}</td>\n<td>{2}</td>\n</tr>".format(filme[0], filme[1], filme[2])
        pass

    template = """<DOCTYPE html>
    <html lang="pt-br">
        <head>
            <title>Lista dos melhores filmes</title>

            <style>
                * {
                    font-family: sans-serif;
                }
                h1 {
                    font-family: sans-serif;
                }
                table {
                    border: 1px solid #333333;
                    border-collapse: collapse;
                }
                table thead {
                    background: sandybrown;
                }
                td {
                    border: 1px solid #333333;
                    padding: 5px;
                }
            </style>
        </head>
        <body>
            <h1>Lista com os 20 melhores filmes de todos os tempos!</h1>
            <table>
                <thead>
                    <tr>
                        <td>Título</td>
                        <td>Lançamento</td>
                        <td>Descrição</td>
                    </tr>
                </thead>
                <tbody>
                    data_list
                </tbody>
            </table>
        </body>
    </html>"""
    return template.replace('data_list', template_lista)  # Troca o data_list pela lista dos filmes


def envia_email(filmes, msg):
    """Responsável por enviar o e-mail"""
    msg = email.message.Message()

    password = config.PASSWORD
    msg['From'] = config.EMAIL_FROM
    msg['To'] = config.EMAIL_TO
    msg['Subject'] = 'Lista de filmes'

    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(message)

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

    print(f'Successfully sent email to {msg["To"]}')


filmes = get_filmes(URL)
message = monta_msg(filmes)

envia_email(filmes, message)
