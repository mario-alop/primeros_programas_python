a = int(input('Primer número: '))
b = int(input('Segundo número: '))
c = int(input('Tercer número: '))

if a > b:
    if a > c:
        maximo = a 
    else:
        maximo = c 
else:
    if b > c :
        maximo = b
    else:
        maximo = c
    
print('El maximo es: ', maximo)
