#https://aprendeconalf.es/docencia/python/ejercicios/diccionarios/
facturas = {}
userin = input("Desea pagar una factura(-), añadir una nueva(+) o terminar la aplicación(.)")
while userin == "+":
    num = input("Cual es el número de la factura?: ")
    price = input("Cual es el precio de esta factura?: ")
    facturas[num] = price
    print("Estas son sus facturas: ")
    print(facturas)
    userin = input("Desea pagar una factura(-), añadir una nueva(+) o terminar la aplicación(.)")
while userin == "-":
    num= input("Cual es el número de la factura que quiere pagar?")
    facturas.pop(num)
    print("Perfecto daremos esa factura como pagada, ahora esta es su lista de facturas")
    print(facturas)
    userin = input("Desea pagar una factura(-), añadir una nueva(+) o terminar la aplicación(.)")
if userin ==".":
    exit