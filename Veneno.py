import random

from Arma import Arma

class Veneno(Arma):
    def __init__(self):
        self.damage = 50
        self.precision = 1
        self.alcance = 1
        self.peso = 5
        self.municion = "Infinita"
        self.cargador = 1
        self.name = "Veneno"

    def __str__(self):
        return f"\nArma: {self.name}, municion: {self.municion}, Cargador: {self.cargador}, Alcance: {self.alcance}, Daño: {self.damage}"

    def disparar(self):
        pass

    def recargar(self):
        pass

    def calcularDamage(self):
        self.municion = 0
        damage = 0
        probabilidad = random.random()
        if probabilidad <= self.precision:
            damage = self.damage
        return damage

