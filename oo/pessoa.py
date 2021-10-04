class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Ola Mundo {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Leonardo')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    p.nome = 'Leonardo'
    print(p.nome)
    print(p.idade)
