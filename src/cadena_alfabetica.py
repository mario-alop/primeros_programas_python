cadena = input('Introduce una palabra: ')
alfabetica = True
for i in range(len(cadena)-1):
    if cadena[i] > cadena[i + 1]:
        alfabetica =False
    else:
        alfabetica = True
print(alfabetica)