print("Ejercicio: Las Manzanas")
print("=" * 50)

pedido = int(input("Indica el número de manzanas que deseas solicitar: "))
stock = 50

if stock < pedido:
    print("Lo sentimos, no contamos con la cantidad suficiente para tu pedido")
else:
    print("Gracias por tu compra, tu pedido se esta procesando")