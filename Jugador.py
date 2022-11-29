import random

from AK47 import AK_47
from Cachetada import Cachetada
from ChanclaVoladora import ChanclaVoladora
from Cuchillo import Cuchillo
from Veneno import Veneno
from Francotirador import Francotirador
from Pistola import Pistola



class Jugador():
    municionAK_47Jugador1 = 0
    municionAK_47Jugador2 = 0

    def __init__(self):
        self.vida = 1000
        self.armadura = 50
        '''random.randint(0,50)'''
        self.curaciones = 5
        '''random.randint(0,5)'''
        self.arma = Pistola()
        self.position = 30
        '''random.randint(0, 500)'''

    def calcularMovimiento (self):
        resultado = 20 - ((self.armadura//100)*10) - self.curaciones - self.arma.peso
        if(resultado <= 0):
            return 1
        return resultado
    def __str__(self):
        return f"vida: {self.vida}, curacion: {self.curaciones}, movimiento: {self.calcularMovimiento()} " \
               f" posicion: {self.position},  armadura: {self.armadura} {str(self.arma)}"
    def avanzar(self, **kargs):
        n = int(input(f"Deme el N maximo {self.calcularMovimiento()}"))
        if n < 0:
            print("Pierdes el turno por ingresar un movimiento negativo, idiota!!")
        else:
            if n <= self.calcularMovimiento():
                self.position += n
            else:
                print("Ese numero no estaba en el rango para avanzar, solo avanzas 1 lugar por idiota!!")
                self.position += 1
    def retroceder (self, **kargs):
        n = int(input(f"Deme el N maximo {self.calcularMovimiento()}"))
        if n < 0:
            print("Pierdes el turno por ingresar un movimiento negativo, idiota!!")
        else:
            if n < self.calcularMovimiento():
                self.position -= n
            else:
                print("Ese numero no estaba en el rango para retroceder, solo retrocedes 1 lugar por idiota!!")
                self.position -= 1

    def seleccionarArma(self, **kwargs):
        armas = {
            1: Pistola(),
            2: Francotirador(),
            3: AK_47(),
            4: Cuchillo(),
            5: Cachetada(),
            6: ChanclaVoladora(),
            7: Veneno()
        }
        arma = armas.get(random.randint(1, 7))
        return arma

    def cambiarArma(self, **kwargs):
        self.arma = self.seleccionarArma()
        print("Se cambio de arma a: ", self.arma.name)

    def recargarArma(self, **kwargs):
        if self.arma.name != "Cachetada" and self.arma.name != "Cuchillo" and self.arma.name != "Chancla voladora"\
                and self.arma.name != "Eutanasia":
            if self.arma.cargador == 0:
                self.arma.recargar()
                print("Se ha recargado el arma")
            else:
                print("Solo se puede recargar el arma cuanto tenga 0 balas en el cargador")
        else:
            print("Esta arma no se pueden recargar, eres un idiota!!, por eso pierdes el turno.\n")

    def atacarConElArma(self, **kwargs):
        if self.arma.cargador == 0:
            print("Tienes que recargar el arma idiota!!, pierdes el turno por no estar pendiente del cargador de tu arma.")
            return False
        else:
            self.arma.disparar()
            return True

    def curarJugador(self, **kwargs):
        if self.vida <= 950:
            if self.curaciones > 0:
                self.vida += 50
                self.curaciones -=1
                print("Se curó.")
            else:
                print("No tienes mas curaciones, pierdes el turno por no prestar atención a tus curaciones.")
        else:
            print("Debes de tener al menos 950 de vida para curarte idiota, pierdes el turno")

