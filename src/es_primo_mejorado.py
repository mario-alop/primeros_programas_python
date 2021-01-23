# Saber si un número es primo.
numero = int(input('Introduce un número: '))

if numero > 1:
    es_primo = True
    divisor = 2
    while divisor < numero:
        if numero % divisor == 0:
            es_primo = False
            break
        divisor += 1
else:
    es_primo = False

    
if es_primo:
    print('El número {0} es primo.'.format(numero))
else:
    print('El número {0} no es primo.'.format(numero))
