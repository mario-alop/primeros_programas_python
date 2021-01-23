from math import pi

radio = float(input('Introduzca el radio de un círculo: '))

# Menú
print('Escoge una opción:')
print('a) Calcula el diámetro.')
print('b) Calcula el perímetro')
print('c) Calcula el área.')
opcion = input('Introduzca la opción (a, b ó c) y pulse intro.')

if opcion == 'a': # Cálculo del diámetro.
    diametro = 2 * radio
    print('El diámetro es {0}.'.format(diametro))
elif opcion == 'b': # Cálculo del perímetro.
    perimetro = 2 * pi * radio
    print('El perímetro es {0}.'.format(perimetro))
elif opcion == 'c': # Cálculo del área.
    area = pi * radio ** 2
    print('El área es {0}.'.format(area))
else:
    print('Solo hay tres opciones: a, b o c.')
    print('Tú has tecleado "{0}".'.format(opcion))

