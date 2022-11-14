#https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/
di = input("Cuanto dinero introduciras en la cuenta de ahorro?")
m1= ((int(di)/100)*104)
m2=((int(m1)/100)*104)
m3=((int(m2)/100)*104)
print("Perfecto pues tus ahorros se veran asi tras el primer ano "+ str(m1) +" euros, tras el segundo ano " + str(m2) +" euros y tras el tercer ano habras ahorrado " + str(m3)+ " euros.")
