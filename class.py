# primeira classe 
class Pessoa(object):
    def __init__(self,nome,idade):
        self.nome  = nome
        self.idade = idade

p1=Pessoa("marcelo",25)
print(p1.nome)