from flask_sqlalchemy import SQLAlchemy

lista = [1,2,3,44,56,6,7,8234,12,3,54]
def increment(x):
    return x+1

list2 = list(filter(lambda x: x%2==0, lista))

print(list2)
class Produto_corte:
    def __init__(self, nome, valor_mat, medida, tempo, valor_hora, custos_extras, lucro):
        self.valor_mat = valor_mat
        self.medida = medida #mm**2
        self.tempo = tempo
        self.valor_hora = valor_hora # -> hora máquina
        self.custos_extras = custos_extras

        self.lucro = lucro
        self.nome = nome





