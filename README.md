# Primeira Automacão com Python
Meu primeiro contato com automação Python e Selenium.

Nesse repositório terá minha primeira experiência com automação usando a linguagem de programação Python e o Selenium.

Objetivo: Desenvolver mesmo que de forma simples uma automatização em cima da rede social Whatsapp Web.

Requisitos para execução da automação:
Será importante instalação no seu ambiente os itens listados para executar a solução.
- Python
- Selenium;
- Webdriver_manager
- Navegador Firfox

## Passo a Passo
1. Utilizando o terminal:

    Caso não tenha o Python instalado acesse o link : https://www.python.org/

2. Clone o projeto:

    git clone https://github.com/FilipeAndre-Silva/Primeira_Automacao_Python.git
  - Entrar na pasta do projeto.
  
  
3. Criar a virtualenv do projeto:

    python3 -m venv .venv
  
4. Iniciar a virtualenv:
  
    . ./venv/bin/activate


5. Atualizar o pip:
  
    pip3 install --upgrade pip
  
6. Instalar os requisitos: 
  
    pip install Selenium
  
    pip install webdriver_manager

7. Executar o .py:
  
    python3 whatsapp_bot.py
  
8. Após executar o .py o navegador Firefox vai abrir o whatsapp web, onde vai aguardar a sua autenticação pelo QR Code.
  
    O Bot do Whatsapp agora está ativo no seu navegador :)
  
    Essa versão do Bot Whatsapp está respondendo automaticamente TODAS AS MENSAGENS (inclusive de grupos) com um texto predeterminado.
  
    Para encerrar, basta fechar o navegador Firefox.
    
- Para alterar a mensagem do bot basta abrir em qualquer editor de texto o arquivo whatsapp_bot.py:
  
  Dentro de whatsapp_bot.py existe uma variável chamado mensagem_bot(linha 8) onde contem o texto resposta da automação.
  
  **Obrigado por ter chegado até aqui :) abraço.**
  
  **Em breve melhorias no comportamento e condições dessa automação, dessa forma a solução terá maior eficiência e usabilidade**
  
