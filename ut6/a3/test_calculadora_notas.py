from calculadora_notas import calcular_media

def test_media_simple():
    assert calcular_media([6,7,8]) == 7

def test_media_decimal():
    assert calcular_media([10,9,8,7]) == 8.5

## Debajo de esta línea debes añadir los tests que hagan que la cobertura suba al 90%

def test_empty_list():
    try:
        calcular_media([])
        assert False
    except ValueError:
        assert True

def test_out_range():
    try:
        calcular_media([-1, 20])
        assert False
    except ValueError:
        assert True

def test_have_str():
    try:
        calcular_media([10, 'a,', 'b', 6])
        assert False
    except ValueError:
        assert True