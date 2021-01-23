numero = int(input('Introduzca un número entero positivo: '))

n_factorial = 1

while numero > 1:
    n_factorial *= numero
    numero -=1
    
print(n_factorial)
print('Hecho')