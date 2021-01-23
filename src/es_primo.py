# Saber si un número es primo.
numero = int(input('Introduce un número: '))

if numero > 1:
    es_primo = True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            es_primo = False
            break
else:
    es_primo = False
    
if es_primo:
    print('El número {0} es primo.'.format(numero))
else:
    print('El número {0} no es primo.'.format(numero))