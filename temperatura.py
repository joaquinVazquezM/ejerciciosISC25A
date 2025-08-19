print("Ejercicio: La temperatura")
print("=" * 50)

tempAyer = int(input("Indica la temperatura de ayer: "))
tempHoy = int(input("Indica la temperatura de hoy "))

if tempAyer > tempHoy:
    print("El día de ayer fue más caluroso")
elif tempAyer == tempHoy:
    print("La temperatura es la misma que ayer")
else:
    print("La temperatura de hoy, es más calurosa")

