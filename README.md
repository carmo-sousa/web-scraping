# Script para web scraping

![Flask](https://img.shields.io/static/v1?label=Sousa&message=Web%20Scraping&style=flat&color=E59500&labelColor=green)
[![GitHub license](https://img.shields.io/github/license/Carmo-sousa/web-scraping)](https://github.com/Carmo-sousa/web-scraping/blob/master/LICENSE)

Faz uma requisição para [Adoro cinema](http://www.adorocinema.com/filmes/todos-filmes/notas-espectadores/)
e envia uma email contendo a lista dos filmes.

![Logo](src/img/logo.svg)

## Setup

1. Vá para a seção [Acesso a app menos seguro](https://myaccount.google.com/lesssecureapps) da sua Conta do Google e ative a opção de aplicativos menos seguros.
2. Ter o [python 3.x](https://www.python.org/) instalado em sua maquina.
3. Clonar o repositório `git clone git@github.com:Carmo-sousa/web-scraping.git`
4. Entrar no diretório `cd web-scraping`
5. Executar `pip install -r requirements.txt` dentro do diretório do projeto.

Criar um arquivos com o nome `.env` na raiz do projeto com os dados abaixo trocando pelas suas credenciais.

```.env
MAIL_FROM = exemplo@email.com
PASSWORD = exemplo_senha
MAIL_TO = exemplo@email.com

URL = http://www.adorocinema.com/filmes/todos-filmes/notas-espectadores/
```

## Execução

Basta executar o comando `python app.py` na raiz do projeto.

## Contribuir

Quer contribuir com o projeto? [Confira o passo a passo](./CONTRIBUTING.md)
Quer ver o que está por vir? [Acompanhe aqui](https://github.com/Carmo-sousa/web-scraping/projects)

## Versionamento

Esse projeto não possui um sistema de versionamento.

## Histórico

Da uma olhada na aba [Releases](https://github.com/Carmo-sousa/web-scraping/releases) pra acompanhar as alterações feitas no projeto.

## Licença do Projeto

[MIT License](./LICENSE) © Rômulo do Carmo Sousa
