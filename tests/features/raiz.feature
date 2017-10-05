Feature: Raiz de dos numeros
    Como usuario de la calculadora
    deseo realizar la raiz de dos numeros
    para obtener el resultado preciso

    Scenario: Raiz de 4 raiz dos
        Dado que ingreso los numeros "4" raiz "2"
        cuando realizo la operación
        entonces obtengo el resultado "2"

        Scenario: Raiz de 0 raiz dos
            Dado que ingreso los numeros "0" raiz "2"
            cuando realizo la operación
            entonces obtengo el resultado "0"

        Scenario: Raiz de 25 raiz dos
            Dado que ingreso los numeros "25" raiz "2"
            cuando realizo la operación
            entonces obtengo el resultado "5"
