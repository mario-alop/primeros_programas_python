'''
# Forma corta de ver si es Palindromo.

texto = input("Ingrese una palabra: ").lower()
rever = texto[::-1]
if texto == rever:
    print("La palabra ingresada si es palindromo!!")
else:
    print("La palabra ingresada no es palindromo!!")

'''
igual = 0 
aux = 0
texto = input("Ingrese la palabra que desea evaluar: ")
for ind in reversed(range(0, len(texto))):
    if texto[ind].lower() == texto[aux].lower():
        igual += 1
    aux += 1
if len(texto) == igual:
    print("El texto es palindromo!")
else:
    print("El texto no es palindromo!")