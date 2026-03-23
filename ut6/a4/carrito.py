def calcular_subtotal(carrito):

    subtotal = 0

    for producto in carrito:
        subtotal += producto["precio"] * producto["cantidad"]

    return subtotal


def aplicar_descuento(subtotal, descuento):
    if descuento < 0 or descuento > 100:
        raise ValueError("Descuento inválido")

    # Multiplicamos para hallar el descuento
    return subtotal * ( 1 - descuento / 100)



def calcular_envio(subtotal):

    
    if subtotal > 100:
        return 0

    return 5


def calcular_total(carrito, descuento):

    subtotal = calcular_subtotal(carrito)

    subtotal_descuento = aplicar_descuento(subtotal, descuento)

    envio = calcular_envio(subtotal_descuento)

    return subtotal_descuento + envio

