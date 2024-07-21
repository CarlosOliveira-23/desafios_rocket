from exame import Exame


def aprovar_solicitacao_exame(exame: Exame):
    if exame.verifica_condicoes():
        print(f"Exame {exame.tipo} aprovado!")
    else:
        print(f"Exame {exame.tipo} reprovado.")


class AprovaExame:
    pass
