# Desglose mimnimo en billets y monedas con un for.

cantidad = int(input('Cantidad de euros: '))

lista = [500, 200, 100, 50, 20, 10, 5, 2, 1]

for i in lista:
    if cantidad >= i:
        queda = cantidad // i
        print('Existen: ' + str(queda) +
               (' Billete' if cantidad >= 5 else ' moneda') + ('s' if queda > 1 else '') +
               ' de  ' + str(i) + ' €')
        cantidad = cantidad % i
