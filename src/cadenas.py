
a = 'mi cadena'
print(a)
print('Frase del reves.')
for i in range(len(a)-1, -1, -1):
    print(a[i], end='')

print()
frase = 'Hola esto es una cadena de prueba.'
print(frase)
print('Contador de espacios.')
sumando = 0   
for i in frase:
    if i == ' ':
        sumando += 1
print(sumando)

texto = 'Una cadena de Prueba con números 1234.'
print(texto)
print('Contador de Mayusculas.')
mayusculas = len([c for c in texto if c.isupper()])
print(mayusculas)
print('Contador de minusculas.')
minusculas = len([c for c in texto if c.islower()])
print(minusculas)
print('Contador de números.')
numeros = len([c for c in texto if c.isdigit()])
print(numeros)