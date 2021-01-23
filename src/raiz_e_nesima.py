numero = int(input('Introduce el número: '))

for i in range(2, 101, 2):
    print('La raíz de {0}-énesima de {1} es {2}'.format(i, numero, numero **(1/i)))
