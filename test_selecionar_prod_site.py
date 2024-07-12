#1 - libs
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


#2 - classes
class Teste_Produtos():
# 2.1 Atributos
    url =   "https://www.saucedemo.com/"

# 2.2 funções e métodos
    def setup_method(self):# os dois pontos dizem onde está a função/ dentro do paranteses recebe e passa valores
        self.driver = webdriver.Chrome() #tem que importar         #instanciar o webdriver com o chrome
        self.driver.implicitly_wait(5)                       #define o tempo de espera padrão dos elementos em segundos

    def teardown_method(self):
        self.driver.quit()                              #fecha o navegador

    def test_selecionar_produto(self):
        self.driver.get(self.url)
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user") #ESCREVE NO CAMPO USERNAME
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce") #ESCRE