from abc import ABC, abstractmethod


class Exame(ABC):
    def __init__(self, tipo):
        self.tipo = tipo

    @abstractmethod
    def verifica_condicoes(self):
        pass
