# -*- coding: utf-8 -*-
from lettuce import step, world
from Calculadora import Calculadora

@step(u'cuando realizo la operación')
def cuando_realizo_la_operacion(step):
    pass

@step(u'Dado que ingreso los numeros "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.suma(int(num1), int(num2))

@step(u'Dado que ingreso los numeros "([^"]*)" menos "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.resta(int(num1), int(num2))

@step(u'Dado que ingreso los numeros "([^"]*)" por "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.multiplicacion(int(num1), int(num2))

@step(u'Dado que ingreso los numeros "([^"]*)" entre "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.division(int(num1), int(num2))

@step(u'Dado que ingreso los numeros "([^"]*)" raiz "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.raiz(int(num1), int(num2))

@step(u'Dado que ingreso los numeros "([^"]*)" elevado "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.potencia(int(num1), int(num2))

@step(u'entonces obtengo el resultado "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
    assert int(esperado) == world.cal.obtener_resultado(),'El resultado esperado es ' +esperado+ ' y el obtenido es ' +str(world.cal.obtener_resultado())
