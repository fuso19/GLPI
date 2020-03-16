'''
Funcoes glpi
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui


class Botglpi:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        self.glpi = webdriver.Chrome(chrome_options=options)

    def Login(self):
        glpi = self.glpi
        glpi.get('GLPI_URL')
        time.sleep(5)  # deixar a pagina carregar

        c_username = glpi.find_element_by_xpath(
            '//input[@id="login_name"]')
        c_password = glpi.find_element_by_xpath(
            '//input[@type="password"]')
        c_username.clear()
        c_password.clear()
        c_username.send_keys(self.username)
        c_password.send_keys(self.password)

        glpi.find_element_by_xpath('//input[@type="submit"]').click()
        time.sleep(4)

    def Chamado_Ativos(self):
        glpi = self.glpi
        # abre chamado
        glpi.get('TICKET_URL')
        time.sleep(2)

        # processando chamado
        glpi.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div[2]/ul/li[5]/a').click()

        time.sleep(15)
        # tarefa
        glpi.find_element_by_class_name('task').click()
        time.sleep(2)

        # escreve Acompanhamento Ativos
        pyautogui.click(559, 555, button='left')
        time.sleep(2)
        pyautogui.typewrite('DESCRIPTION')
        time.sleep(1)
        # Adicionar tarefa
        glpi.find_element_by_xpath('//input[@type="submit]"').click()


ativos = Botglpi('LOGIN_ID', 'PASSWORD')
ativos.Login()
ativos.Chamado_Ativos()
