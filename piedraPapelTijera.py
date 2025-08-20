print("=" * 50)
print("Bienvenidos al juego piedra papel o tijera ")
print("=" * 50)

jugador1 = input("Elije, piedra, papel o tijera: 🎮 ")
jugador2 = input("Elije, piedra, papel o tijera: 🎮 ")

print(f"El jugador 1, ha elejido: ", jugador1)
print(f"El jugador 2, ha elejido: ", jugador2)

if jugador1 == jugador2:
    print("Empate ambos eligieron lo mismo")
elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "tijera" and jugador2 == "papel") or (jugador1 == "papel" and jugador2 == "piedra"):
    print("Jugador uno es el ganador")
else:
    print("El jugador dos, es el ganador")