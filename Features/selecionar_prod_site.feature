Feature: Selecionar Produto


    Scenario: Selecionar prodto "Sauceq labs Backpack"
        Given que acesso o site Sauce Demo
        When preencho os campos de login com usuario standard_user e senha secret_sauce
        Then sou direcionado para pagina Home