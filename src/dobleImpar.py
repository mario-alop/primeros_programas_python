# Doble de un número impar

numero = int(input('Dame un número par: '))

if numero % 2 == 0:
    if (numero / 2) % 2 != 0:
        print(f'ok, {numero} es el doble de un número impar')
    else:
        print(f'el {numero} no es el doble de un número impar')    

else:
    print(f'el {numero} no es par')