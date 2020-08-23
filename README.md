# Script para web scraping

Faz uma requisição para [Adoro cinema](http://www.adorocinema.com/filmes/todos-filmes/notas-espectadores/)
e envia uma email com um template HTML contendo a lista dos filmes.

![Exemplo da resposta](img/exemplo-02.png)

## Pré requisitos

Habilitar o uso de apps menos seguros.
1. Vá para a seção [Acesso a app menos seguro](https://myaccount.google.com/lesssecureapps) da sua Conta do Google. Talvez seja necessário fazer login.
2. Desative a opção Permitir aplicativos menos seguros.

Ter o [python 3.x](https://www.python.org/).

Ter o [BeautfulSoup4](https://pypi.org/project/beautifulsoup4/).

Ter o [requests](https://pypi.org/project/requests/).

## Configurando

Crie um arquivo com o nome `config.py` e salve suas credencias dentro.
![Exemplo do arquivo config.py](/img/exemplo-01.png)

Troque os campos de acordo com os seus dados.

## Atenção

O modulo `smtplib.py` está com o modo de encode 'ASCII'
sendo assim não reconhece alguns caracteres e pode gerar um erro.

Uma forma de corrigir é editando o modulo
![Exemplo de como o arquivo deve ficar depois da alteração](img/error.png)
trocando o trecho `msg = _fix_eols(msg).encode('ASCII')` por `msg = _fix_eols(msg).encode('utf-8')`
que o erro deve ser resolvido.

## Execução

Entre na pasta do projeto e de o comando `python main.py`.

FIM!!
