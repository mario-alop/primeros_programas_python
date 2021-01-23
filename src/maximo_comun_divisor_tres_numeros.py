numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))
numero3 = int(input("Número 3: "))
 
if numero1 < numero2 and numero1 < numero3:
    mcd = numero1
elif numero2 < numero1 and numero2 < numero3:
    mcd = numero2
else:
    mcd = numero3
while True:
    if numero1%mcd == 0 and numero2%mcd == 0 and numero3%mcd == 0:
        print("El mcd es", mcd)
        break
    else:
        mcd -= 1
