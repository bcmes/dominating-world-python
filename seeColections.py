# Listas sao heterogeneas
list = [123, 12.23, 'bruno', False]
for e in list:
    print(e)

# deletando um elemento da lista
print('deletando item')
del list[1]
for e in list:
    print(e)
# add elemento na lista
print('add elemento na lista')
list.append('X')
for e in list:
    print(e)
# junta duas listas
list1=[1,2,3]
list2=[4,5,6]
list3=list1+list2
for e in list3:
    print(e)
# mesma coisa acima, porem altera a lista1
list1.extend(list2)
for e in list1:
    print(e, end='-')

# enum: tem key e value.: um enum nao pode ser lido 2x for um for, pois seu iterator fica com o valor fim.
print('enum:')
myEnum = enumerate(['a', 'b', 'c'])
# assim so le uma vez: e é uma tupla
for e in myEnum:
    print(e)
# nao vai faz nada...
for e in myEnum:
    print(e)

# posso fazer spreading no for
print('enum com for spreading:')
myEnumX = enumerate(['a1', 'b2', 'c3'])
# assim so le uma vez
for k, v in myEnumX:
    print(k, v)

# modo simples de imprimir uma colecao
myCollection = ['1','2','s',1,3,2]
print(*myCollection)

# dictionaries, semelhante a map/objeto
meuDicionario = {'chave1': 'valor1','chave2': 'valor2'}
meuDicionario2 = dict(chave1='valor1',chave2='valor2')
pessoa = {
    'nome': 'Bruno',
    'sexo': 'M',
    'idade': 12,
    'contatos': [
        {
            'celular': 123456,
            'email': 'email@email.com'
        }
    ]
}
print(meuDicionario)
print(meuDicionario2)
print(pessoa)
print(pessoa['contatos'][0]['celular'])
# em um for com dicionarios, é retornado as chaves
for p in pessoa:
    print(p)

# pode-se definir dinamicamente os elementos de um dicionario
carros={}
carros['modelo'] = 'BMW'
print(carros)
# pode-se deletar dinamicamente um item do dicionario
del carros['modelo']
print(carros)
# consultando elemento de forma segura (nao retorna erro se a key nao existir)
carros.get('modelo') # retorno default None se nao existir
carros.setdefault('modelo', 'default') # quando for chamado, se nao for definido, retorna um valor default
print(carros['modelo'])
