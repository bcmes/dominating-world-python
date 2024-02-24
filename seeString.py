# interpolacao
a = 'Bruno'
b = 'Campos'
texto = 'a={} b={}'.format(a, b)
print(texto)

# para nao depender da ordem informe o indice
texto = 'a={1} b={0}'.format(a, b)
print(texto)

# alias para os parametros
texto = 'a={nome} b={sobrenome}'.format(nome=a, sobrenome=b)
print(texto)

# outra forma de interpolacao
value = 10.9
texto2 = 'O preço é R$ %s' % value
print(texto2)

# valor e decimal e hexa
value2 = 78
print('%d = %x = %f' % (value2, value2, value2))
print('%d = %X = %f' % (value2, value2, value2))

# repete o valor da string
print('Bruno ' * 3)

# replace de valores
nome = "Bruno"
salario = 60000.234521
texto = f'meu nome é {nome} e meu salario é {salario:,.2f}'
print(texto)

# char especifico da string
print('Array de string:')
carro = 'Gol bola'
print(carro[2])
# indice contando de tras pra frente
print(carro[-3])
# substring
print(carro[1:])
print(carro[1:5])
print(carro[:5])
# passo, o padrao é 1
print(carro[0:8:1])
# pegou um, pulou um
print(carro[0:8:2])
# inverte a string
print(carro[::-1])

# ver se o char existe no array string
print('a' in carro)

# ver se o char nao existe no array string
print('a' not in carro)

# especamento fixo a direita
myText1 = "0123"
myText2 = "01"
myText3 = "01235678"
print(f'{myText1}')
print(f'{myText2: >5}')
print(f'{myText3: >5}')
# especamento fixo a esquerda
print(f'{myText2: <5}')
print(f'{myText3: <5}')
# especamento fixo centro
print(f'{myText2: ^5}')
print(f'{myText3: ^5}')
# especamento fixo com preenchimento
print(f'{myText2:@^5}')
print(f'{myText3:@^5}')

# conta caracteres
print(len('bruno'))