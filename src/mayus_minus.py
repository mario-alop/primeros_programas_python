
letra = str(input('Introduzca una letra: '))

if letra >= 'a' and letra <= 'z':
    print('Es una MINÚSCULA.')
else:
    if letra >= 'A' and letra <= 'Z':
        print('Es una MAYÚSCULA.')
    else:
        if letra == "Ñ":
            print ('Es una eñe MAYÚSCULA.')
        else:
            if letra == "ñ":
                print('Es una eñe MINÚSCULA.')
            else:
                print('No es una letra.')


