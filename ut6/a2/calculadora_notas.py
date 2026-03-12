
def calcular_media(notas):

    if len(notas) == 0:
        raise ValueError("Lista vacía")

    suma = 0

    for nota in notas:

        if nota < 0 or nota > 10:
            raise ValueError("Nota fuera de rango")

        suma += nota

    return suma // len(notas)

    return media
# Programa principal para realizar pruebas

# Pon el código aquí y borra esta línea