from exame import Exame


class ExameRaioX(Exame):
    def __init__(self):
        super().__init__("raio-x")

    def verifica_condicoes(self):
        print("Verificando condições para exame de raio-x...")
        return True
