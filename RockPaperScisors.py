import random
user_option = "S"

while user_option == "S":

    print("1. Piedra")
    print("2. Papel")
    print("3. Tijeras")
    user_choice = int(input("Digite su elección   "))

    valor = random.choice(["Piedra", "Papel", "Tijeras"])

    if valor == "Piedra" and user_choice == 1:
        print(f"Empate, tu elegiste Piedra y la maquina ha sacado {valor}")
    elif valor == "Piedra" and user_choice == 2:
        print(f"Ganaste, tu elegiste Papel y la maquina ha sacado {valor}")
    elif valor == "Piedra" and user_choice == 3:
        print(f"Perdiste, tu elegiste Tijeras y la maquina ha sacado {valor}")
    elif valor == "Papel" and user_choice == 1:
        print(f"Ganaste, tu elegiste Papel y la maquina ha sacado {valor}")
    elif valor == "Papel" and user_choice == 2:
        print(f"Empate, tu elegiste Papel y la maquina ha sacado {valor}")
    elif valor == "Papel" and user_choice == 3:
        print(f"Empate, tu elegiste Papel y la maquina ha sacado {valor}")
    elif valor == "Tijeras" and user_choice == 1:
        print(f"Ganaste, tu elegiste Piedra y la maquina ha sacado {valor}")
    elif valor == "Tijeras" and user_choice == 2:
        print(f"Perdiste, tu elegiste Papel y la maquina ha sacado {valor}")
    else:
        print(f"Empate, tu elegiste Tijeras y la maquina ha sacado {valor}")

    user_option = str(input("\n¿Quieres seguir jugando? Presiona S para seguir jugando   "))