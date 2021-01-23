
n = int(input('Introduzca el número de intervalo: '))
m = int(input('Introduzca el número limite: '))
i = 0
if n > m:
    print('El limite debe ser mayor que el intervalo.')
    #n = int(input('Introduzca el número de intervalo: '))
    #m = int(input('Introduzca el número limite: '))
else:
    while i <= m:
        print(i)
        i += n
    
print('Hecho')
