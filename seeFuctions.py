# coisas definidas dentro da funcao respeitam o escopo da funcao.
# posso definir funcao dentro de funcao
# posso receber como parametro de uma funcao outra funcao
# uma funcao pode retornar outra funcao

variavelExterna = 0

# Função simples
def olaMundo():
    print("Hello world.")

# Com argumentos
def olaMundo2(name, sex):
    print(f'Ola {name} do sexo {sex}')

# Com argumentos com valores defaults
def olaMundo3(name='nome X', sex='?'):
    print(f'Ola {name} do sexo {sex}')

# Definindo None (nada) como default
def olaMundo4(name=None, sex=None):
    if name is not None and sex is not None:
        print(f'Ola {name} do sexo {sex}')
    else:
        print('defina os parametros')

# Alterando o escopo de uma variavel. Ao inves de seu escopo ser interno a sua funcao, sera o global
def escopoNormal():
    variavelExterna = 10
    print(f'escopo interno: {variavelExterna}')
def escopoAlterado():
    global variavelExterna # estou modificando a variavel externa, do começo deste arquivo
    variavelExterna = 10
    print(f'escopo interno: {variavelExterna}')

# funcoes sem retorno
def funcao1(): # retorna None( tipo void )
    print('operacao')

# funcoes com retorno
def funcao2(): # retorna String
    return 'operacao'

# funcoes com argumentos infinitos
def funcao3(*args): #os elementos estao em uma tupla
    print(sum(args))

# funcao que retorna outra funcao
def oneFunction(cumprimentos):
    def interFunction(nome):
        return f'{cumprimentos} {nome}'
    return interFunction



# chamando funcoes
olaMundo()
olaMundo2('Bruno', 'M')
olaMundo2(sex='M', name='Bruno') # Pode-se chamar a funcao indicando o nome do argumento, assim nao precisa seguir a ordem.
olaMundo3()
olaMundo4()
print('Escopos:')
print(f'Variavel externa: {variavelExterna}')
escopoNormal()
print(f'Variavel externa: {variavelExterna}')
escopoAlterado()
print(f'Variavel externa: {variavelExterna}')

print(f'analisando retorno da funcao: {funcao1()}')
funcao3(1,2,3,4,4,5)

interFunction = oneFunction('Boa tarde')
result = interFunction('Bruno')
print(result)