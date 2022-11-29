import random

from Arma import Arma

class Francotirador(Arma):
    def __init__(self):
        self.damage = 200
        self.precision = 0.9
        self.alcance = 200
        self.peso = 10
        self.municion = "Infinita"
        self.cargador = 1
        self.name = "Francotirador"

    def __str__(self):
        return f"\nArma: {self.name}, municion: {self.municion}, Cargador: {self.cargador}, Alcance: {self.alcance}, Daño: {self.damage}"

    def disparar(self):
        self.cargador -= 1

    def recargar(self):
        self.cargador = 1

    def calcularDamage(self):
        self.municion = 0
        damage = 0
        probabilidad = random.random()
        if probabilidad <= self.precision:
            damage = self.damage
        return damage

