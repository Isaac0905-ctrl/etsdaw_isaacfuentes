def calcular_subtotal(carrito):
    subtotal = 0
    for producto in carrito:
        if not isinstance(producto['nombre'], str) or not isinstance(producto['precio'], (int, float)):
            raise ValueError('Valores no aceptados en el carrito')
        if producto['precio'] < 0 or producto['cantidad'] < 0:
            raise ValueError('No pueden ser negativos')
        precio = producto["precio"]
        cantidad = producto["cantidad"]
        subtotal += precio * cantidad
    return subtotal


def aplicar_descuento(subtotal, descuento):
    if descuento < 0 or descuento > 100:
        return subtotal
    return subtotal - (subtotal * descuento / 100)


def aplicar_cupon(subtotal, cupon):
    if cupon == "WELCOME10":
        return subtotal * 0.9
    elif cupon == "FREESHIP":
        return subtotal
    else:
        return subtotal


def calcular_envio(subtotal):
    if subtotal >= 100:
        return 0
    return 5


def calcular_impuestos(subtotal):
    return round(subtotal * 0.07, 2)


def calcular_total(carrito, descuento=0, cupon=None):
    subtotal = calcular_subtotal(carrito)
    subtotal = aplicar_descuento(subtotal, descuento)

    if cupon:
        subtotal = aplicar_cupon(subtotal, cupon)

    envio = 0 if cupon == "FREESHIP" else calcular_envio(subtotal)

    base_a_pagar = subtotal + envio
    impuestos = calcular_impuestos(base_a_pagar)

    return round(base_a_pagar + impuestos, 2)
