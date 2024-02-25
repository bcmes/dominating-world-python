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