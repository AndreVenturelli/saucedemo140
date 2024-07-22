from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('que acesso o site Sauce Demo')
def step_acess_site(context):
        context.driver = webdriver.Chrome()
        context.driver.get('https://www.saucedemo.com/')


@when('preencho os campos de login com usuario "{username}" e senha "{password}"')
def step_login(context, username, password):
        context.driver.find_element(By.ID, "username").send_keys(username)
        context.driver.find_element(By.ID, "password").send_keys(password)
        context.driver.find_element(By.ID, "login-button").click()

@when('adiciono o produto "Sauce Labs Backpack" ao carrinho')
def step_add_to_cart(context)
        assert context.driver.find_element(By.ID, "inventory-item-name").text == "Sauce Labs Backpack"
        assert context.driver.findelement(By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_price").text == "$29.99"
        context.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()