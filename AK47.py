import random

from Arma import Arma

class AK_47(Arma):
    def __init__(self):
        self.damage = 17
        self.precision = 0.3
        self.alcance = 100
        self.peso = 5
        self.municion = 300
        self.cargador = 60
        self.name = "AK-47"
        self.balasAdisparar = 0

    def __str__(self):
        return f"\nArma: {self.name}, municion: {self.municion}, Cargador: {self.cargador}, Alcance: {self.alcance}, Daño: {self.damage}"

    def disparar(self):
        self.balasAdisparar = int(input("¿Cuantas valas quieres disparar?"))


    def recargar(self):
        gastado = 60 - self.cargador
        self.municion -= gastado
        self.cargador = 60

    def calcularDamage(self):
        damage = 0
        balasAcertadas = 0
        print("Balas a disparar: ", self.balasAdisparar)
        if self.balasAdisparar > self.cargador:
            print("No puedes disparar esa cantidad de veces, pierdes el turno por no estar pendiente idiota!!")
        else:
            self.cargador -= self.balasAdisparar
            for x in range (0, self.balasAdisparar):
                probabilidad = random.random()
                if probabilidad <= self.precision:
                    damage += self.damage
                    balasAcertadas += 1
            print("Acertaste ", balasAcertadas, " balas.")
        return damage
