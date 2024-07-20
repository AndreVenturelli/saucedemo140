import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Test_buy_product():

    url =   "https:www.giulianaflores.com.br"


    def setup_method(self):
        self.driver = webdriver.Chrome() 
        self.driver.implicitly_wait(5)                       

    def teardown_method(self):
        self.driver.quit()                              

    def teste_buy_product(self):
        self.driver.get(self.url)
        self.driver.find_element(By.CSS_SELECTOR, ".swiper-wrapper .swiper-slide:nth-child(2) .img_banner").click()
        self.driver.find_element(By.CLASS_NAME, "close-button").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ulPrincipal .item:nth-child(3) .product-item").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input_cep .campos-cep .box-field-mobile input:nth-of-type(1)").send_keys("18022")
        self.driver.find_element(By.CSS_SELECTOR, ".input_cep .campos-cep .box-field-mobile input:nth-of-type(2)").send_keys("200")
        self.driver.find_element(By.ID, "ContentSite_lbtBuy").click