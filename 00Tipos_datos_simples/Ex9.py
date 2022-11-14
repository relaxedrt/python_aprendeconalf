#https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/
yn = input("Vamos a ganar dinero, te apetece?")
if yn == "yes" or yn == "si":
    d = input("Cuanto dinero vas a invertir?")
    i = input("Cuanto porcentaje de interes anual buscas?")
    t = input("Cuantos anos lo vas a tener invertido?")
    print ("Perfecto pues en " + str(t) + " anos tendras" + str(float(d)+(float(d)*float(i)*float(t))) + "euros")
else:
    print("Tu te lo pierdes socio")