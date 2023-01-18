#https://aprendeconalf.es/docencia/python/ejercicios/programacion-funcional/
#Completar creando  una funcion que anada a la lista original 
#los precios de cada piso y luego con otra  funcion se busque 
#cuales son mas baratos del presupuesto y anadirlos a una lista nueva
pisos = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]
def calcprecios(l):
    lp = []
    for i in l:
        if i["zona"] == "A":
            p = ((i["metros"] * 1000) + (i["habitaciones"]*5000) + (int(i["garaje"])*15000)) * (1 - (2023 - i["año"]) / 100)
            i["precio"] = p
            lp.append(i)
        if i["zona"] == "B":
            p = (((i["metros"] * 1000) + (i["habitaciones"]*5000) + (int(i["garaje"])*15000)) * (1 - (2023 - i["año"]) / 100) ) * 1.5 
            i["precio"] = p
            lp.append(i)
    return lp
def busqueda(l, p):
    nl = []
    for i in l:
        if i["precio"] <= p:
            nl.append(i)
    return nl

    


print(busqueda(calcprecios(pisos), 100000))