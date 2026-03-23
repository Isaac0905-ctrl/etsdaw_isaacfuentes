import pytest
from carrito import calcular_subtotal
def test_carrito_productos():
    assert calcular_subtotal([
        {"nombre":"portatil","precio":100,"cantidad":2},
        {"nombre":"monitor","precio":50,"cantidad":1}]) == 250

def test_carrito_producto():
    assert calcular_subtotal([
    {"nombre":"Cascos JBL","precio":135,"cantidad":1}]) == 135

def test_carrito_vacio():
    assert calcular_subtotal([]) == 0

from carrito import aplicar_descuento

def test_descuento_cero():
    assert aplicar_descuento(100, 0) == 100

def test_descuento_valido():
    assert aplicar_descuento(100, 15) == 85

def test_descuento_cien():
    assert aplicar_descuento(100, 100) == 0

def test_descuento_invalido():
    with pytest.raises(ValueError):
        aplicar_descuento(100, 110)


from carrito import calcular_envio

def test_envio_menor_cien():
    assert calcular_envio(99) == 5

def test_envio_cien_o_mas():
    assert calcular_envio(101) == 0



from carrito import calcular_total

def test_total_sin_descuento():
    carrito = [{"nombre": "pro", "precio": 50, "cantidad": 1}]
    assert calcular_total(carrito, 0) == 55

def test_total_con_descuento():
    carrito = [{"nombre": "pro", "precio": 100, "cantidad": 1}]
    assert calcular_total(carrito, 20) == 85

def test_total_envio_gratis():
    carrito = [{"nombre": "pro", "precio": 200, "cantidad": 1}]
    assert calcular_total(carrito, 10) == 180
