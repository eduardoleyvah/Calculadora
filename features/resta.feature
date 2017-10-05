Feature: Resta de dos numeros
    Como usuario de la calculadora
    deseo realizar la resta de dos numeros
    para obtener el resultado preciso

    Scenario: Resta de 2 menos dos
        Dado que ingreso los numeros "2" menos "2"
        cuando realizo la operación
        entonces obtengo el resultado "0"

    Scenario: Resta de 7 menos cinco
        Dado que ingreso los numeros "7" menos "5"
        cuando realizo la operación
        entonces obtengo el resultado "2"

    Scenario: Resta de 5 menos 7
        Dado que ingreso los numeros "5" menos "7"
        cuando realizo la operación
        entonces obtengo el resultado "- 2"

    Scenario: Resta de 1000 menos 100
        Dado que ingreso los numeros "1000" menos "100"
        cuando realizo la operación
        entonces obtengo el resultado "900"
