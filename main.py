from Jugador import Jugador

def error(**kwargs):
    print("La opcion no es válida, perdiste el turno")

def atacar(jugador1: Jugador, jugador2 : Jugador):
    distancia = abs(jugador1.position - jugador2.position)
    if jugador1.arma.alcance > distancia:
        resul = jugador1.atacarConElArma()
        if resul:
            damage = jugador1.arma.calcularDamage()
            if (damage == 0):
                print("Fallaste idiota!! no le diste.")
            else:
                print("Le diste!!")
                if jugador2.armadura > 0:
                    if damage >= jugador2.armadura:
                        damage -= jugador2.armadura
                        jugador2.vida -= damage
                        jugador2.armadura = 0
                        print("Le has roto la armadura al otro jugador.")
                    else:
                        jugador2.armadura -= damage
                        print("Le has causado daño a la armadura del jugador")
                else:
                    jugador2.vida = jugador2.vida - damage
    else:
        print("El jugador que deseas atacar no esta en el rango de ataque, pierdes el turno por "
              "no estar pendiente de la posicion de los jugadores, idiota!!\n")

def turno(jugador1: Jugador, jugador2: Jugador):
    opciones = {
        1: atacar,
        2: jugador1.avanzar,
        3: jugador1.retroceder,
        4: jugador1.recargarArma,
        5: jugador1.cambiarArma,
        6: jugador1.curarJugador
    }

    print("1. Atacar")
    print("2. Avanzar")
    print("3. Retroceder")

    print("4. Recargar")
    print("5. Cambiar de arma")
    print("6. Curarse")
    print("Digite la acción a realizar: \n")
    metodo = opciones.get(int(input()), error)
    jugadores = {
        "jugador1": jugador1,
        "jugador2": jugador2,
    }
    metodo(**jugadores)

if __name__ == '__main__':
    jugador1 = Jugador()
    jugador2 = Jugador()
    while (jugador1.vida > 0 and jugador2.vida > 0):
        print("-----------------------------------------------------------------------------------------------------")
        print("DATOS DE LOS JUGADORES")
        print("\nJUGADOR 1: \n", jugador1)
        print("\nJUGADOR 2: \n", jugador2)
        print("-----------------------------------------------------------------------------------------------------")
        if jugador1.vida <= 0:
            print("El juego ha acabado, y ha ganado el jugador 2, FELICITACIONES!!")
            break
        else:
            print("\nEL TURNO ES DEL JUGADOR 1:\n")
            turno(jugador1,jugador2)
            if jugador1.arma.name == "Veneno":
                jugador1.vida -= jugador1.arma.damage
                print("Recibes 50 de daño y tu arma se vuelve a cambiar. Eso te pasa por querer cambiar de arma a cada instante idiota!!")
                jugador1.cambiarArma()
        if jugador2.vida <= 0:
            print("El juego ha acabado, y ha ganado el jugador 1, FELICITACIONES!!")
            break
        else:
            print("-----------------------------------------------------------------------------------------------------")
            print("DATOS DE LOS JUGADORES")
            print("\nJUGADOR 1: \n", jugador1)
            print("\nJUGADOR 2: \n", jugador2)
            print("-----------------------------------------------------------------------------------------------------")
            print("\nEL TURNO ES DEL JUGADOR 2:\n")
            turno(jugador2, jugador1)
            if jugador2.arma.name == "Veneno":
                jugador2.vida -= jugador2.arma.damage
                print( "Recibes 50 de daño y tu arma se vuelve a cambiar. Eso te pasa por querer cambiar de arma a cada instante idiota!!")
                jugador2.cambiarArma()

