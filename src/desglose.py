
# Desglose mimnimo en billets y monedas.

cantidad = int(input('Cantidad de euros: '))

quinientos = 0
doscientos = 0
cien = 0
cincuenta = 0
veinte = 0
diez = 0
cinco = 0
dos = 0
uno = 0
auxiliar = 0

if (cantidad // 500) > 0:
    quinientos = cantidad // 500
    cantidad = cantidad - (quinientos * 500)
if (cantidad // 200) > 0:
    doscientos = cantidad // 200
    cantidad = cantidad - (doscientos * 200)
if (cantidad // 100) > 0:
    cien = cantidad // 100
    cantidad = cantidad - (cien * 100)
if (cantidad // 50) > 0:
    cincuenta = cantidad // 50
    cantidad = cantidad - (cincuenta * 50)
if (cantidad // 20) > 0:
    veinte = cantidad // 20
    cantidad = cantidad - (veinte * 20)
if (cantidad // 10) > 0:
    diez = cantidad // 10
    cantidad = cantidad - (diez * 10)
if (cantidad // 5) > 0:
    cinco = cantidad // 5
    cantidad = cantidad - (cinco * 5)
if (cantidad // 2) > 0:
    dos = cantidad // 2
    cantidad = cantidad - (dos * 2)
if (cantidad // 1) > 0:
    uno = cantidad // 1
    cantidad = cantidad - (uno * 1)
print('Esta cantidad contiene:')
print(quinientos,' billetes de 500 €.')
print(doscientos,' billetes de 200 €.')
print(cien,' billetes de 100 €.')
print(cincuenta,' billetes de 50 €.')
print(veinte,' billetes de 20 €.')
print(diez,' billetes de 10 €.')
print(cinco,' billetes de 5 €.')
print(dos,' monedas de 2 €')
print(uno,' monedas de 1 €.')



