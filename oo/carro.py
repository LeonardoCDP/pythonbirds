'''
    >>> # Testando Motor:
    >>> motor = Motor()

    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0

    >>> # Testando a Direção:
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'

    >>> # Testando Carro:
    >>> carro = Carro(motor, direcao)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    3
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    1
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Sul'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Oeste'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Sul'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
'''

NORTE = 'Norte'
LESTE = 'Leste'
SUL = 'Sul'
OESTE = 'Oeste'


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade < 2:
            self.velocidade -= 1
        else:
            self.velocidade -= 2


class Direcao:
    rotacao_a_direita_dct = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }
    rotacao_a_esquerda_dct = {
        NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE
    }

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]


    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]


class Carro():
    def __init__(self, motor, direcao):
        self.motor = motor
        self.direcao = direcao

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_velocidade(self):
        return self.motor.velocidade

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

    def calcular_direcao(self):
        return self.direcao.valor


if __name__ == '__main__':
    import doctest

    doctest.testmod()
