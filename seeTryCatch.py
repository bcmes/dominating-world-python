# captura qualquer excecao
stringNumber = input('Digite um numero inteiro: ')

try:
    print('valid number = ', int(stringNumber))
except:
    print('invalid number')