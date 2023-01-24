#https://aprendeconalf.es/docencia/python/ejercicios/ficheros/
import csv
archivo = "cotizacion.csv"
dic = {}
nombre = []
final = []
maximo = []
minimo = []
volumen = []
efectivo = []
with open(archivo, newline='') as File:
    data = csv.reader(File)
    for row in data:
        if row != ['Nombre;Final;Máximo;Mínimo;Volumen;Efectivo']:
            ro= "".join(row)
            r = ro.split(";")
            nombre.append(r[0])
            final.append(r[1])
            maximo.append(r[2])
            minimo.append(r[3])
            volumen.append(r[4])
            efectivo.append(r[5])
dic["Nombre"] = nombre
dic["Final"] = final
dic["Maximo"] = maximo
dic["Mínimo"] = minimo
dic["Volumen"] = volumen
dic["Efectivo"] = efectivo