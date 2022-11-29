import random
from Arma import Arma

class Cachetada(Arma):
    def __init__(self):
        self.damage = 15
        self.precision = 0.8
        self.alcance = 25
        self.peso = 2
        self.municion = "Infinita"
        self.cargador = "Infinito"
        self.name = "Cachetada"

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