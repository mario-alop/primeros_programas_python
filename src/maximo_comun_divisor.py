
'''
def mcd(a,b):
    if b == 0:
        return a
    else:
        return mcd(b, a%b)

a = int(input('Introduce el primer número: '))
b = int(input('Introduce el segundo número: '))

print('El MCD de {0} y {1} es: {2}'.format(a, b, mcd(a, b)))
'''

num1 =int(input('Introduce el primer número: '))
num2 =int(input('Introduce el segundo número: '))

num_max = max(num1, num2)
num_min = min(num1, num2)

while num_min:
    mcd = num_min
    num_min = num_max % num_min
    num_max = mcd
mcm =  (num1 * num2) // mcd

print('El Maximo Comun Divisor de {0} y {1} es {2}'.format(num1, num2, mcd))
print('El Minimo Comun Multiplo de {0} y {1} es {2}'.format(num1, num2, mcm))

