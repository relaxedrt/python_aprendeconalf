#https://aprendeconalf.es/docencia/python/ejercicios/ficheros/
import csv
archivo = "08Ficheros/cotizacion.csv"
dic = {}
nombre = []
final = []
maximo = []
minimo = []
volumen = []
efectivo = []
mf = 0
mmax = 0
mmin = 0
mv = 0
me = 0
with open(archivo, newline='') as File:
    data = csv.reader(File)
    for row in data:
        if row != ['Nombre;Final;Máximo;Mínimo;Volumen;Efectivo']:
            ro= "".join(row)
            ro = ro.replace(".","")
            ro = ro.replace(",",".")
            r = ro.split(";")
            nombre.append(r[0])
            final.append(float(r[1]))
            maximo.append(float(r[2]))
            minimo.append(float(r[3]))
            volumen.append(float(r[4]))
            efectivo.append(float(r[5]))
dic["Nombre"] = nombre
dic["Final"] = final
dic["Maximo"] = maximo
dic["Mínimo"] = minimo
dic["Volumen"] = volumen
dic["Efectivo"] = efectivo
mf = sum(final)/len(final)
mmax = sum(maximo)/len(maximo)
mmin = sum(minimo)/len(minimo)
mv = sum(volumen)/len(volumen)
me = sum(efectivo)/len(efectivo)