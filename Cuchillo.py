import random

from Arma import Arma

class Cuchillo(Arma):
    def __init__(self):
        self.damage = 250
        self.precision = 0.98
        self.municion = "Infinito"
        self.cargador = "Infinito"
        self.alcance = 5
        self.peso = 0
        self.name = "Cuchillo"

    def __str__(self):
        return f"\nArma: {self.name}, municion: {self.municion}, Cargador: {self.cargador}, Alcance: {self.alcance}, Daño: {self.damage}"
    def disparar(self):
        pass

    def recargar(self):
        pass

    def calcularDamage(self):
        damage = 0
        probabilidad = random.random()
        if probabilidad <= self.precision:
            damage = self.damage
        return damage

