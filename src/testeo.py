'''
Created on 23 ene. 2021

@author: mario
'''

# Testeo 2

x = [1, 2, 3]
y = x[:]
print(y)
print('-----------------------')
def mi_funcion(param1, param2, *param_n):
    print(param1)
    print(param2)
    print('-----------------------')
    for x in param_n:
        print(x)
    return
mi_funcion(1, 2, 3, 4, 5, "Mario")
