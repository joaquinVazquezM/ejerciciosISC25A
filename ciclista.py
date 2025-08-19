print("Ejercicio ciclista")
print("=" * 50)

velocidadUno = int(input("Ingrese la velocidad del ciclista 1 "))
velocidadDos = int(input("Ingrese la velocidad del ciclista 2 "))

if velocidadUno > velocidadDos:
    print("El ciclista uno es más rápido")
elif velocidadUno == velocidadDos:
    print("Empate, ambos van iguales")
else:
    print("El ciclista dos es más rápido")