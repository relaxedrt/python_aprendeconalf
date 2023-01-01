#https://aprendeconalf.es/docencia/python/ejercicios/funciones/
money = int(input("Cual es el precio de la factura sin iva?: "))
imp = int(input("Que porcentaje de iva le corresponde?: "))
def calc(bruto,iva = 21):
    total = bruto+((bruto/100)*iva)
    print(f"{total} Euros.")
#Primer ejemplo en el que le damos los dos argumentos
calc(money,imp)
#Segundo ejemplo en el que uno de los argumentos lo toma por defecto
calc(money)