

cadena = input('Introduzca una cadena: ')

i = int(input('Introduzca primer número: '))
j = int(input('Introduzca segundo número: '))

if i < 0:
    inicio = 0
else:
    inicio = i

if j > len(cadena):
    final = len(cadena)
else:
    final = j

subcadena = ''

for indice in range(inicio, final):
    subcadena += cadena[indice]
    
print('la cadena: {0}, desde la posición: {1}, hasta la posición: {2}: {3}'
      .format(cadena, inicio, final, subcadena))
    

