# if
expresao = True
if expresao:
    print("True")

# if-elseIf
expresao = 2
if expresao > 2:
    print("Maior")
elif expresao <= 2:
    print("Menor")

# if-elseIf-else
expresao = 2
if expresao > 2:
    print("Maior")
elif expresao < 2:
    print("Menor")
else:
    print("Igual")

# Se uma instrução for muito grande para uma linha, ela pode ser quebrada, igual vc faria com comandos de terminal
nomeQueFicouMuitoGrande = "x"
nomeQueFicouMuitoGrande2 = "x"
nomeQueFicouMuitoGrande3 = "x"
if nomeQueFicouMuitoGrande2 == nomeQueFicouMuitoGrande \
    and nomeQueFicouMuitoGrande3 == nomeQueFicouMuitoGrande:
    print('Funciona !')

# Condicao ternaria
condicao = False
valor = 'valor1' if condicao else 'valor2'
print(valor)