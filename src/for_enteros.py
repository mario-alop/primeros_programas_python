
n = int(input('Introduce el número n: '))
m = int(input('Introduce el número m: '))


for i in range(n, m):
    print(i)

print('----------------------')

for i in range(n, m):
    print(i**2)
    
print('----------------------')

sumatorio = 0

for i in range(n, m):
    if i % 2 == 0:
        sumatorio += i
print(sumatorio)