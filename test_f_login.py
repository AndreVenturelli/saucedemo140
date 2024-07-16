import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#2 - classes
class Teste_f_login():
# 2.1 Atributos
    url =   "https:www.giulianaflores.com.br"

# 2.2 funções e métodos
    def setup_method(self):# os dois pontos dizem onde está a função/ dentro do paranteses recebe e passa valores
        self.driver = webdriver.Chrome() #tem que importar         #instanciar o webdriver com o chrome
        self.driver.implicitly_wait(5)                       #define o tempo de espera padrão dos elementos em segundos

    def teardown_method(self):
        self.driver.quit()                              #fecha o navegador

    def test_f_login(self):
        self.driver.get(self.url)
        self.driver.find_element(By.ID, "perfil-display").click()
        self.driver.find_element(By.ID, "UrlLogin").click()
        self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("teste@teste.com")
        self.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("123456")
        self.driver.find_element(By.ID, "ContentSite_ibtContinue").click()
        #Um teste onde esperamos o erro do usuario em realizar o login
