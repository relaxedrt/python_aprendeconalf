#https://aprendeconalf.es/docencia/python/ejercicios/cadenas/
fecha = input("Introduce tu fecha de cumple en el siguiente formato dd/mm/aaaa : ")
lFecha = fecha.split("/")
mes = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio",
        "Agosto","Septiembre","Octubre","Noviembre","Diciembre")
mesfix = int(lFecha[1]) - 1
#PRIMERA IDEA DE HACERLO MUY ABURRIDA Y POCO EFICIENTE
# if lFecha[1] == "1":
#     print("Tu cumpleanos es el " + lFecha[0] + " de " + mes[0] + " del " + lFecha[2])
# elif lFecha[1] == "2":
#     print("Tu cumpleanos es el " + lFecha[0] + " de " + mes[1] + " del " + lFecha[2])
# elif lFecha[1] == "3":
#     print("Tu cumpleanos es el " + lFecha[0] + " de " + mes[2] + " del " + lFecha[2]) 
# elif lFecha[1] == "4":
#     print("Tu cumpleanos es el " + lFecha[0] + " de " + mes[3] + " del " + lFecha[2]) 
# elif lFecha[1] == "5":
#     print("Tu cumpleanos es el " + lFecha[0] + " de " + mes[4] + " del " + lFecha[2]) 
# elif lFecha[1] == "6":
#     print("Tu cumpleanos es el " + lFecha[0] + " de " + mes[5] + " del " + lFecha[2]) 
# elif lFecha[1] == "7":
#     print("Tu cumpleanos es el " + lFecha[0] + " de " + mes[6] + " del " + lFecha[2]) 
# elif lFecha[1] == "8":
#     print("Tu cumpleanos es el " + lFecha[0] + " de " + mes[7] + " del " + lFecha[2]) 
# elif lFecha[1] == "9":
#     print("Tu cumpleanos es el " + lFecha[0] + " de " + mes[8] + " del " + lFecha[2])
# elif lFecha[1] == "10":
#     print("Tu cumpleanos es el " + lFecha[0] + " de " + mes[9] + " del " + lFecha[2]) 
# elif lFecha[1] == "11":
#     print("Tu cumpleanos es el " + lFecha[0] + " de " + mes[10] + " del " + lFecha[2]) 
# elif lFecha[1] == "12":
#     print("Tu cumpleanos es el " + lFecha[0] + " de " + mes[11] + " del " + lFecha[2])
print("Tu cumpleanos es el " + lFecha[0] + " de " + mes[mesfix] + " del " + lFecha[2])     