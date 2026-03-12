from calculadora_notas import calcular_media

def test_media_simple():
    assert calcular_media([7, 5, 6]) ==  6

def test_media_con_decimales():
    assert calcular_media([7, 5, 6, 4]) == 5,5

def test_one_note():
    assert calcular_media([2]) == 2

def test_empty_list():
    try:
        calcular_media([])
        assert False
    except ValueError:
        assert True

def test_out_range():
    try:
        calcular_media([-1,15])
        assert False
    except ValueError:
        assert True

