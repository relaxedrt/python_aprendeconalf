#https://aprendeconalf.es/docencia/python/ejercicios/diccionarios/
compra = {}
total = 0
fin = 1
while fin == 1:
    obj = input(f"Que quieres comprar?: ")
    price = int(input(f"Cuanto cuesta?: "))
    fin = int(input(f"Quieres seguir comprando? no=0/ si=1: "))
    compra[obj] = price
for i in compra.values():
    total += i
print(f"{compra}")
print(f"El precio total de la compra es {total} euros.")