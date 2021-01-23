cadena = input('Introduce una cadena: ')

inversion = ''
for caracter in cadena:
    print(caracter)
    inversion = caracter + inversion

print('Su inversión es: ', inversion)
