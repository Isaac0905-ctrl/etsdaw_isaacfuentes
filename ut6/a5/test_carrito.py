import pytest
from carrito import calcular_subtotal

def test_varios_productos():
     assert calcular_subtotal([
    {"nombre":"teclado","precio":50,"cantidad":2},
    {"nombre":"raton","precio":130,"cantidad":1}
    ]) == 230
     
def test_carrito_producto():
     assert calcular_subtotal([
 {"nombre":"monitor AOC","precio":550,"cantidad":1}]) == 550 

def test_carrito_vacio():
     assert calcular_subtotal ([]) == 0

def test_valores_invalidos():
     carrito_con_errores = [
    {"nombre":"Tv","precio":-30,"cantidad":-2},
    {"nombre":"raton","precio":10,"cantidad":1}]
     with pytest.raises(ValueError):
        calcular_subtotal(carrito_con_errores)

from carrito import aplicar_descuento

import pytest

def aplicar_descuento(subtotal, descuento):
    if descuento < 0 or descuento > 100:
        return subtotal
    return subtotal - (subtotal * descuento / 100)

@pytest.mark.parametrize("subtotal_descuento, esperado", [
     ((200, 0), 200),
     ((350, 13), 304.5),
     ((100, 100), 0),
     ((550, -10), 550),
     ((425, 500), 425),
])
def test_varios_(subtotal_descuento, esperado):
     subtotal, descuento = subtotal_descuento
     resultado = aplicar_descuento(subtotal, descuento)
     assert resultado == esperado

#def test_descuento_0():
#     assert aplicar_descuento(200, 0) == 200

#def test_descuento_valido():
#     assert aplicar_descuento(350, 13) == 304.5

#def test_descuento_100():
#     assert aplicar_descuento(100, 100) == 0

#def test_descuento_invalido():
#     assert aplicar_descuento(550, -10) == 550

#def test_descuento_mayor_cien():
#     assert aplicar_descuento(425, 150) == 425"""

from carrito import aplicar_cupon

def test_cupon_bienvenida():
     assert aplicar_cupon(500,'WELCOME10') == 450

def test_envio_gratis():
     assert aplicar_cupon(200,'FREESHIP') == 200

def test_cupon_invalido():
     assert aplicar_cupon(950, 'HOLA') == 950

import pytest
from carrito import (
    calcular_envio, calcular_impuestos, calcular_total
)

@pytest.mark.parametrize("subtotal, envio_esperado", [
    (50, 5),
    (100, 0),
    (150, 0),
])
def test_calcular_envio(subtotal, envio_esperado):
    assert calcular_envio(subtotal) == envio_esperado

def test_calcular_impuestos():
    assert calcular_impuestos(100) == 7.00
    assert calcular_impuestos(33.33) == 2.33

def test_completo():
    carrito = [{"nombre": "Teclado", "precio": 100, "cantidad": 1}]
    total = calcular_total(carrito, 10, "WELCOME10")
    assert total == 92.02

def test_total_cupon_freeship():
    carrito = [{"nombre": "Mouse", "precio": 20, "cantidad": 1}]
    assert calcular_total(carrito, 0, "FREESHIP") == 21.4

def test_con_descuento_y_cupon():
    carrito = [
        {"nombre": "Diccionario", "precio": 30, "cantidad": 2},
        {"nombre": "Set de Auriculares", "precio": 10, "cantidad": 1}
    ]
    total = calcular_total(carrito, 10, "WELCOME10")
    assert total == 66.02

def test_negativo():
    carrito_invalido = [{"nombre": "Error", "precio": -50, "cantidad": 1}]
    with pytest.raises(ValueError):
        calcular_total(carrito_invalido)


