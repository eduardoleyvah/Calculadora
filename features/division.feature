Feature: Division de dos numeros
    Como usuario de la calculadora
    deseo realizar la division de dos numeros
    para obtener el resultado preciso

    Scenario: Division de 2 entre dos
        Dado que ingreso los numeros "2" entre "2"
        cuando realizo la operación
        entonces obtengo el resultado "1"

    Scenario: Division de 4 entre dos
        Dado que ingreso los numeros "4" entre "2"
        cuando realizo la operación
        entonces obtengo el resultado "2"

    Scenario: Division de 0 entre 5
        Dado que ingreso los numeros "0" entre "5"
        cuando realizo la operación
        entonces obtengo el resultado "0"
