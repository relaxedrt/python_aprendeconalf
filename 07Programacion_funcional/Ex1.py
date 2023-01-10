#https://aprendeconalf.es/docencia/python/ejercicios/programacion-funcional/
basket = {1000:20, 500:10, 100:1}
def disc(precio, descuento):
    #Aplicamos al precio el descuento y lo devolvemos
    return precio - precio * descuento/100
def imp(precio, impuesto):
    #Aplicamos al precio el impuesto y lo devolvemos
    return precio + precio * impuesto/100
def cesta(dic, func):
    #Aplicamos a la cesta de la compra la funcion de impuestos o descuento
    cestafin = []
    
    for precio, porcentaje in dic.items():
        cestafin.append(func(precio, porcentaje))
    return (cestafin,sum(cestafin))

print(f"Aqui esta la cesta con iva: {cesta(basket, imp)}")
print(f"Aqui esta la cesta con descuento: {cesta(basket, disc)}")
