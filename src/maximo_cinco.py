a = int(input('Primer número: '))
b = int(input('Segundo número: '))
c = int(input('Tercer número: '))
d = int(input('Cuarto número: '))
f = int(input('Quinto número: '))

mayor = a
if b > mayor:
    mayor = b
if c > mayor:
    mayor = c 
if d > mayor:
    mayor = d
if f > mayor:
    mayor = f 
maximo = mayor

print('El maximo es: ', maximo)