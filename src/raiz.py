from math import sqrt

num = -1
while num < 0:
    num = float(input('Introduce un número positivo: '))
    
print('La raiz cuadrada de {0} es {1}'.format(num, sqrt(num)))
