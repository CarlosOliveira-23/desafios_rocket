from exame import Exame


class ExameSangue(Exame):
    def __init__(self):
        super().__init__("sangue")

    def verifica_condicoes(self):
        print("Verificando condições para exame de sangue...")
        return True
