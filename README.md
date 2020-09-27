# Primeira Automacão com Python
Meu primeiro contato com automação Python e Selenium.

Nesse repositôrio terá minha primeira experiência com automação usando a linguagem de programação Python e a ferramenta Selenium.

Objetivo: Desenvolver mesmo que de forma simples uma automatizaçã sobre a rede social Whatsapp Web.

Requesitos para execução da automação:
Será importante a instalação no seu ambiente os itens listados para executar a solução.
- Python
- Selenium;
- Webdriver_manager
- Navegador Firfox

# Passo a Passo

Caso não tenha o Python instalado acesse o link e faça o download:

  https://www.python.org/


- Clone o projeto

  git clone https://github.com/FilipeAndre-Silva/Primeira_Automacao_Python.git
  - Entrar na pasta do projeto.


- Criar a virtualenv do projeto:

  python3 -m venv .venv
  
  
- Iniciar a virtualenv:

  . ./venv/bin/activate


- Atualizar o pip:
  
  pip3 install --upgrade pip
  
  
- Instalar os requisistos:
  
  pip install Selenium
  
  pip install webdriver_manager

- Executar o py:

  python3 whatsapp_bot.py
  
- Apois isso o navegador Firefox vai abrir no link do whatsapp web, onde vai aguardar a sua autenticação pelo QR code.
  
  O Bot do Whatsapp agora está ativo no seu navegador :)
