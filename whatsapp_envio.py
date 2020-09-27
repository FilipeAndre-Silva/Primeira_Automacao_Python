from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://web.whatsapp.com/")
time.sleep(10)

contatos = ['Pai']
mensagem = "Teste do meu Bot"

def pesquisando_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    time.sleep(3)
    campo_mensagem[1].send_keys(Keys.ENTER)

for contato in contatos:
    pesquisando_contato(contato)
    enviar_mensagem(mensagem)