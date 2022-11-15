#https://aprendeconalf.es/docencia/python/ejercicios/bucles/
money = float(input("Cuanto dinero deseas invertir?: "))
interes = float(input("Cuanto interes anual te interesa?: "))
years = int(input("Cuantos anos deseas tenerlo invertido?: "))
for i in range(1,years):
    money = (money*(interes/100))+money
    print(f"Tras {i+1} anos, tendras {money} euros.")