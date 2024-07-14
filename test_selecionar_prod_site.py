#1 - libs
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        self.driver.find_element(By.ID, "login-button").click() #clicque no botão plugin/ No casso, utilizamos o elemento css

        #transição de pagina

        assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products" #confirma se está escrito Products no elemento
        assert self.driver.find_element(By.ID, "item_4_title_link").text == "Sauce Labs Backpack"    #confirma se é a mochila
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_price").text == "$29.99"
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(2) .inventory_item_price").text == "$9.99"
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(3) .inventory_item_price").text == "$15.99"
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(4) .inventory_item_price").text == "$49.99"
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(5) .inventory_item_price").text == "$7.99"
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(6) .inventory_item_price").text == "$15.99"
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-badge\"]").text == "1"
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-badge\"]").text == "2"
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-badge\"]").text == "3"
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-badge\"]").text == "4"
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-badge\"]").text == "5"
        self.driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-badge\"]").text == "6"
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-link\"]").click()
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-badge\"]").text == "5"
        self.driver.find_element(By.ID, "remove-sauce-labs-bike-light").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-badge\"]").text == "4"
        self.driver.find_element(By.ID, "remove-sauce-labs-bolt-t-shirt").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-badge\"]").text == "3"
        self.driver.find_element(By.ID, "remove-sauce-labs-fleece-jacket").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-badge\"]").text == "2"
        self.driver.find_element(By.ID, "remove-sauce-labs-onesie").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-badge\"]").text == "1"
        self.driver.find_element(By.ID, "remove-test.allthethings()-t-shirt-(red)").click()
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        self.driver.find_element(By.ID, "logout_sidebar_link").click()

        
