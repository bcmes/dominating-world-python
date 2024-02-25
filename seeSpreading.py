# normal
nome1, nome2, nome3 = ['maria','joao','pedro']
print(nome1, nome2, nome3)

# somente o primeiro valor
nomea, *_ = ['maria','joao','pedro']
print(nomea, _)

# usando tuplas(imutaveis) ao inves de arrays
nomea1, *_ = 'maria','joao','pedro' #é a mesma coisa que: ('maria','joao','pedro')
print(nomea1, _)

# convertendo listas para tuplas
myList = ['maria','joao','pedro']
myTuple = tuple(myList)
print(myTuple)

# convertendo de tupla para lista
myNewList = list(myTuple)
print(myNewList)