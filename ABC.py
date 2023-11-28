from collections.abc import MutableSequence

class MinhaListinhaMutavel(MutableSequence):
    pass

objetoValidado = MinhaListinhaMutavel()
print(objetoValidado)

#Exemplo para mostrar o ABC = Abstract Base Classes, usando ele para exigir que a classe MinhaListinhaMutavel use todos os metodos abstratos da superclasse MutableSequence
