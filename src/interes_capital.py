

capital_euros = float(input('Introduzca una cantidad: '))
tasa_interes = float(input('Introduzca el tipo de interes: '))
anios = int(input('Introduzca número de años: '))


total = capital_euros * (1 + tasa_interes/100) ** anios

print(total)
print(total)   


