class Pessoa:
    olhos = 2 # atributo de classe

    def __init__(self, *filhos, nome=None, idade=30):
        self.idade = idade # atributo de instancia
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola Mundo {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - {cls.olhos}'

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
    carlos.olhos = 1
    del carlos.olhos
    print(carlos.__dict__) # atributo especial que mostra lista os atributos de instancia
    print(phelipe.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(carlos.olhos)
    print(phelipe.olhos)
    print(id(Pessoa.olhos), id(carlos.olhos), id(phelipe.olhos))
    print(Pessoa.metodo_estatico(), carlos.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), carlos.nome_e_atributos_de_classe())
