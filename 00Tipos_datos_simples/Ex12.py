#https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/
pr = 3.49
disc = 0.6
bv = input("Cuantas barras que no son del dia se han vendido?")
print ("La barra se vende normalmente a " + str(pr) + " euros, con el descuento del " + str(float(disc)*100) + " porciento y el costo total sera de " + str(float(pr)*float(disc)*float(bv)) + " euros.")