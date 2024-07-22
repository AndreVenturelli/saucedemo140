Feature: Adicionar produto ao carrinho no site Sauce Demo

  Scenario: Selecionar produto "Sauce Labs Backpack" e validar no carrinho
    Given que acesso o site Sauce Demo
    When preencho os campos de login com usuario "standard_user" e senha "secret_sauce"
    And adiciono o produto "Sauce Labs Backpack" ao carrinho
    Then o produto "Sauce Labs Backpack" está no carrinho com quantidade "1" e preço "$29.99"