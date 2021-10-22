class Pessoa:
    def __init__(self, *filhos, nome=None, idade=30):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola Mundo {id(self)}'


if __name__ == '__main__':
    phelipe = Pessoa(nome='Phelipe')
    carlos = Pessoa(phelipe, nome='Carlos')
    print(Pessoa.cumprimentar(phelipe))
    print(id(phelipe))
    print(phelipe.cumprimentar())
    print(phelipe.nome)
    print(phelipe.idade)
    for filho in carlos.filhos:
        print(filho.nome)
    carlos.sobrenome = 'Ramalho' # cria atributo dinamico
    print(carlos.sobrenome)
    del carlos.filhos # remove atributo na execução
    print(carlos.__dict__) # atributo especial que mostra lista os atributos de instancia
    print(phelipe.__dict__)
