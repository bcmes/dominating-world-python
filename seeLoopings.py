# while
number = 0
while number < 5:
    print(number)
    number += 1

print('Break: ')
while number != 0:
    print(number)
    number -= 1
    if number == 2:
        break

print('Continue: ')
number = 0
while number < 5:
    number += 1
    if number == 2:
        continue
    print(number)

# while ELSE: Se o wilhe terminar com sucesso o ELSE É EXECUTADO
number = 0
while number < 5:
    print(number)
    number += 1
    # break
else:
    print('terminou com sucesso.')

# FOR
texto = 'bla bala'
for char in texto:
    print(char)

# obtendo um interator do objeto
print('interador:')
casa='Londres'
interador=iter(casa)
print(next(interador))
print(next(interador))

# FOR ELSE
for char in texto:
    print(char)
else:
    print('for concluido com sucesso')