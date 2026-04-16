# UT7A1 – Identificación de “malos olores” en el código


### Objetivo de la práctica

El objetivo de esta práctica es **analizar un programa que funciona correctamente pero cuya calidad de código es mejorable**.

Durante la sesión se realizará un **análisis colectivo del código para detectar “malos olores” (code smells)**. Estos son indicios de que el diseño del programa podría mejorarse mediante técnicas de refactorización.

- En esta práctica **no se debe modificar el código**.  
- El trabajo consiste únicamente en **analizarlo y debatir sobre su calidad**.


### Instrucciones de la práctica

Se proporciona un programa sencillo que simula un **sistema básico de gestión de pedidos**.

El programa realiza varias operaciones:

- almacena una lista de productos
- calcula el precio de cada producto en función de su cantidad
- aplica un descuento en algunos casos
- calcula el coste de envío
- calcula el total del pedido

Aunque el programa funciona correctamente, su código presenta **diversos problemas de diseño y calidad**.

El objetivo de la práctica es **analizar el código para identificar esos problemas**.

### Trabajo en clase

1. Lee el código detenidamente.
2. Analiza cómo está organizado.
3. Detecta posibles problemas de diseño o calidad del código.
4. Anota todos los problemas que encuentres.

Durante la sesión se realizará un **debate en clase**, donde cada grupo expondrá los problemas detectados.

### Preguntas que pueden ayudarte en el análisis

Para identificar posibles problemas puedes plantearte las siguientes cuestiones:

- ¿Hay **métodos demasiado largos**?
- ¿Las **variables tienen nombres claros y descriptivos**?
- ¿Se repite código en diferentes partes del programa?
- ¿Hay **números que aparecen directamente en el código sin explicación**?
- ¿El código mezcla distintas responsabilidades?
- ¿El programa sería fácil de modificar o ampliar?
- ¿Falta documentación o comentarios que expliquen el funcionamiento?

### Entregable

Cada grupo deberá entregar un documento que incluya:

- una lista de los problemas detectados en el código
- una breve explicación de cada problema
- una posible mejora para cada caso

### Nombres pocos descriptivos
    En el constructor de la clase tenemos nombres que se podrian mejorar ya que a primera vista no sabemos que representan y esto hace el codigo menos legible.

    Ejemplos a mejorar:
    - P pasaria a ser producto
    - N pasaría a ser nombre
    - C pasaría a ser cantidad

### Podriamos utilizar constantes para los porcentajes
    Ejemplo:
    En lugar de aplicar 0.1 podemos asignarlo a una variables y de esta manera hacer nuestro código mas profesional

    Descuento = 0.1

    Si el dia de mañana cambia el descuento solo tendriamos que modificar esta constante y no el resto del código

### Constantes para envío gratis
    Asignamos una constante que en este caso represente el valor del envio gratis

    ENVIO_GRATIS = 100


### Añadir funciones que calculen ciertos datos
    Las funciones tienen la finalidad de ayudarnos a la hora de programar y ahorrar codigo ya que las podemos reutilizar

    Podriamos asignar funciones para calcular el total, subtotal, precio de envío y asi tener nuestro código mejor estructurado
    

### Código a analizar

El código a analizar es el siguiente:

```python
class Producto:

    def __init__(self, n, p, c):
        self.n = n
        self.p = p
        self.c = c


productos = []

productos.append(Producto("Teclado", 30, 2))
productos.append(Producto("Raton", 15, 3))
productos.append(Producto("Monitor", 200, 1))

total = 0

for p in productos:

    subtotal = p.p * p.c

    if p.c > 2:
        subtotal = subtotal - (subtotal * 0.1)

    print("Producto:", p.n)
    print("Precio:", p.p)
    print("Cantidad:", p.c)
    print("Subtotal:", subtotal)

    if subtotal > 100:
        print("Envio gratis")
    else:
        print("Envio: 5 euros")
        subtotal = subtotal + 5

    total = total + subtotal

    print("-------------------")

print("TOTAL PEDIDO:", total)

if total > 500:
    print("Cliente VIP")
```