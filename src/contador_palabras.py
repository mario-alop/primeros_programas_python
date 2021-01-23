cadena = input('Introduce una cadena: ')
while cadena != '':
    cambios = 0
    anterior = ''
    for caracter in cadena:
        if caracter == ' ' and anterior != ' ':
            cambios += 1
        anterior = caracter
    
    if cadena[-1] == ' ':
        cambios -= 1
    if cadena[0] == ' ':
        cambios -= 1
        
    palabras = cambios + 1 # Hay una palabra más que cambio de no blanco a blanco.
    print('Palabras: ', palabras)
    cadena = input('Introduce una cadena: ')