from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#Texto que o bot responde ao receber uma nova mesangens.
mensagem_bot = """Olá sou ChatBoot do Filipe!
           Ele está ocupado no momento..., mas ele vai responder em breve.
           Se quiser pode deixar recado :)"""

#Variável que alimenta a condição continua.
comando = 'on'

#Inciando o navegador e abrindo o whatsapp web.
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://web.whatsapp.com/")

#Tempo determinado para o usuário atutenticar o QR code do whatsapp.
time.sleep(15)

#Função para clicar no contato que enviou uma nova mensagem e manda a resposta.
def enviar_mensagem(mensagem):
    element.click()
    time.sleep(3)

    campo_mensagem = driver.find_elements_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].send_keys(mensagem)
    time.sleep(3)
    campo_mensagem[1].send_keys(Keys.ENTER)

#Condição continua que verifica se existe novas mensagens não lidas e inicia a função enviar_mensagem.
#A cada final de reposta recarrega a página.
while comando == 'on':
    try:
        #capturando o icone de nova mensagem.
        element = driver.find_element_by_class_name('_31gEB')
        enviar_mensagem(mensagem_bot)
        time.sleep(5)
        driver.refresh()

    except NoSuchElementException:
        continue


#Falta implementar uma exceção que faça o bot não responder mensagens de Grupos só de Chat Privado



