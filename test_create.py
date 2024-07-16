import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#2 - classes
class test_create():
# 2.1 Atributos
    url =   "https:www.giulianaflores.com.br"

# 2.2 funções e métodos
    def setup_method(self):# os dois pontos dizem onde está a função/ dentro do paranteses recebe e passa valores
        self.driver = webdriver.Chrome() #tem que importar         #instanciar o webdriver com o chrome
        self.driver.implicitly_wait(5)                       #define o tempo de espera padrão dos elementos em segundos

    def teardown_method(self):
        self.driver.quit() 

    def teste_create(self):
        self.driver.get(self.url)
        self.driver.find_element(By.ID, "perfil-display").click()
        self.driver.find_element(By.ID, "UrlLogin").click()
        self.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").click()
        self.driver.find_element(By.ID, "ContentSite_txtName").send_keys("Renan José Assis")
        self.driver.find_element(By.ID, "ContentSite_txtCpf").send_keys("597.330.088-93")
        self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("renan.jose.assis@vbrasildigital.net")
        self.driver.find_element(By.ID, "ContentSite_txtPasswordNew").send_keys("Teste123")
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys("18022-200")
        self.driver.find_element(By.ID, "recaptcha-anchor").click()
        self.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").click()