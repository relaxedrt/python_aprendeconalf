# #https://aprendeconalf.es/docencia/python/ejercicios/cadenas/
# producto = input("Que vas a comprar?: ")
# precio = float(input("Introduce su precio?: "))
# unidades = int(input("Cuantas unidades vas a comprar?: "))
# total = precio * unidades
# print("Vas a comprar " + producto + " por " + {precio:9.} +  " euros cada unidad,y " + unidades + " unidades")
producto = input('Introduce el nombre del producto: ')
precio = float(input('Introducde el precio unitario: '))
unidades = int(input('Introduce el número de unidades: '))
print('{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {total:11.2f}€'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))