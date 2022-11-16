#https://aprendeconalf.es/docencia/python/ejercicios/bucles/
num = int(input("Dame un numero y te dire si es primo o no: "))
for i in range(2,num):
    if (num%i)==0:
        break      
if (i + 1) == num:
    print(f"El numero {num} es primo.")
else:
    print(f"El numero {num} no es primo.")
