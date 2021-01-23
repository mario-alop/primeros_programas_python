import math

n = 1
m = 2

while n < m:
    print('n tiene que ser mayor o igual que m.')
    n = int(input('Introduzca el número n: '))
    m = int(input('Introduzca el número m: '))

diferencia = n - m    
n_factorial = 1

while n > diferencia:
    n_factorial *= n
    n -= 1
print(n_factorial)    

m_factorial = 1

while m > 0:
    m_factorial *= m
    m -= 1
print(m_factorial)

combinacion = n_factorial / m_factorial 

   
#combinacion = math.factorial(n) / (math.factorial(m) * math.factorial(n-m))

print(combinacion)
