import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get("https://www.saucedemo.com/")

#Preencher com usuario e senha    
@when(u'preencho os campos de login com usuario {usuario} e senha {senha}') 
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    context.driver.find_element(By.ID, "password").send_keys(senha)
    context.driver.find_element(By.ID, "login-button").click()

#preencher cm usuario em branco e senha
@when(u'preencho os campos de login com usuario e senha {senha}') 
def step_impl(context, senha):
    context.driver.find_element(By.ID, "password").send_keys(senha)
    context.driver.find_element(By.ID, "login-button").click()


@when(u'preencho os campos de login com usuario {usuario} e senha ') 
def step_impl(context, usuario):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    context.driver.find_element(By.ID, "login-button").click()

@when(u'preencho os campos de login com usuario e senha ') 
def step_impl(context):
     context.driver.find_element(By.ID, "login-button").click()

# Preencher com usuário e senha através da decisão (IF)
@when(u'digito os campos de login com usuario {usuario} e senha {senha} com IF')
def step_impl(context, usuario, senha):
    if usuario != '<branco>':
        context.driver.find_element(By.ID, "user-name").send_keys(usuario)  # preencher o usuário
        # se o usuário estiver em <branco> não há ação de preenchimento

    if senha != '<branco>':
        context.driver.find_element(By.ID, "password").send_keys(senha)     # preencher a senha
        # se a senha estiver em <branco> não há ação de preenchimento

    context.driver.find_element(By.ID, "login-button").click()          # clicar no botão login

@then(u'sou direcionado para pagina Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
    #time.sleep(2)


    context.driver.quit()

@then(u'exibe a mensagem de erro no login')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text =="Epic sadface: Username and password do not match any user in this service"
    

    context.driver.quit()


@then(u'exibe a {mensagem} de erro no login')
def step_impl(context, mensagem):
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == mensagem
    

    context.driver.quit()