# vendo o endereco de memoria
# veja que ele cria um pool para valores comuns
value = 10
value2 = 10
print(id(value))
print(id(value2))

# nao tem escopo de bloco
condition = True
if condition:
    interno = 'valor interno'
    print(interno)
else:
    print('Nao fez o IF')

print(interno)