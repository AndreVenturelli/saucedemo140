import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#2 - classes
class Test_buy_product():
# 2.1 Atributos
    url =   "https:www.giulianaflores.com.br"

# 2.2 funções e métodos
    def setup_method(self):# os dois pontos dizem onde está a função/ dentro do paranteses recebe e passa valores
        self.driver = webdriver.Chrome() #tem que importar         #instanciar o webdriver com o chrome
        self.driver.implicitly_wait(5)                       #define o tempo de espera padrão dos elementos em segundos

    def teardown_method(self):
        self.driver.quit()                              #fecha o navegador

    def teste_create(self):
        self.driver.get(self.url)
        self.driver.find_element(By.CSS_SELECTOR, ".swiper-wrapper .swiper-slide:nth-child(1) .img_banner").click()
        self.driver.find_element(By.ID, "32413").click()