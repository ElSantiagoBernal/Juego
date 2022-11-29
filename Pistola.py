import random
from Arma import Arma

class Pistola(Arma):
    def __init__(self):
        self.damage = 50
        self.precision = 0.5
        self.alcance = 50
        self.peso = 2
        self.municion = "Infinita"
        self.cargador = 9
        self.name = "Pistola"

    def __str__(self):
        return f"\nArma: {self.name}, municion: {self.municion}, Cargador: {self.cargador}, Alcance: {self.alcance}, Daño: {self.damage}"

    def disparar(self):
        self.cargador -= 1

    def recargar(self):
        self.cargador = 9

    def calcularDamage(self):
        damage = 0
        probabilidad = random.random()
        print("prob. pist: ", probabilidad)
        if probabilidad <= self.precision:
            damage = self.damage
        return damage

