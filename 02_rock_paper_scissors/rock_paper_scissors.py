import random

opciones = ["Piedra", "Papel", "Tijera"]

restart = 1

puntos_jugador = 0
puntos_cpu = 0

separador = "-" * 40

while restart == 1:

    print("\n" + separador)
    print("NUEVA PARTIDA")
    print(separador)
    
        
    cpu = random.choice(opciones)
    jugador = int(input("Escoge entre Piedra (1), Papel (2) o Tijera (3): "))

    piedra = 1
    papel = 2
    tijera = 3

    print("El CPU escogió ", cpu)
    
    if jugador == 1 and cpu == "Piedra" or jugador ==2 and cpu == "Papel" or jugador == 3 and cpu =="Tijera":
        print(separador)
        print("Empate")
        print(separador)
        
    elif jugador == 1:
        if cpu == "Tijera":
            print(separador)
            print("Ganaste")
            print(separador)
            puntos_jugador +=1
        else:
            print(separador)
            print("CPU gana")
            print(separador)
            puntos_cpu +=1
    elif jugador == 2:
        if cpu == "Piedra":
            print(separador)
            print("Ganaste")
            print(separador)
            puntos_jugador +=1
        else:
            print(separador)
            print("CPU gana")
            print(separador)
            puntos_cpu +=1
    elif jugador == 3: 
        if cpu == "Papel":
            print(separador)
            print("Ganaste")
            print(separador)
            puntos_jugador +=1
        else:
            print(separador)
            print("CPU gana")
            print(separador)
            puntos_cpu +=1
    else:
        print("Selección inválida, selecciona Piedra, Papel o Tijera")
    
 
    print(f'Marcador: Jugador {puntos_jugador} - {puntos_cpu} CPU')
    print(separador)
    

    restart = int(input("¿Volver a jugar? 1 para SI, 2 para NO "))
    print("\n")
    
    if restart == 2:
        print(f"Marcador final: Jugador {puntos_jugador} - {puntos_cpu} CPU")
        print("Vale, luego seguimos jugando 😀")
        break
    elif restart == 1:
        continue
    
    else:
        print("Selección inválida, vuelve a intentarlo")
        restart = int(input("¿Volver a jugar? 1 para SI, 2 para NO "))
        
