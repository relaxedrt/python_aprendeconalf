#https://aprendeconalf.es/docencia/python/ejercicios/ficheros/
import csv
file = "08Ficheros/calificaciones.csv"
def examenesyasist(f):
    with open(f, newline='') as File:
        lista = []
        data = csv.reader(File)
        for row in data:
            if row != ["Apellidos;Nombre;Asistencia;Parcial1;Parcial2;Ordinario1;Ordinario2;Practicas;OrdinarioPracticas"]:
                row1= "".join(row)
                #ro = row1.replace(",",".")
                r = row1.split(";")
                dic = {}
                #####################################
                dic["Apellidos"] = r[0]
                #####################################
                dic["Asistencia"] = r[2]
                #####################################
                if int(r[3]) > 10:
                    dic["Parcial1"] = float(r[3])/100
                else:
                    dic["Parcial1"] = float(r[3])
                #####################################
                if int(r[4]) > 10:
                    dic["Parcial2"] = float(r[4])/100
                else:
                    dic["Parcial2"] = float(r[4])
                #####################################
                if r[5] != "":
                    if int(r[5]) > 10:
                        dic["Ordinario1"] = float(r[5])/100
                    else:
                        dic["Ordinario1"] = float(r[5])
                else:
                    dic["Ordinario1"] = 0.0
                #####################################
                if r[6] != "":
                    if int(r[6]) > 10:
                        dic["Ordinario2"] = float(r[6])/100
                    else:
                        dic["Ordinario2"] = float(r[6])
                else:
                    dic["Ordinario2"] = 0.0
                #####################################
                if r[7] != "":
                    if int(r[7]) > 10:
                        dic["Practicas"] = float(r[7])/100
                    else:
                        dic["Practicas"] = float(r[7])
                else:
                    dic["Practicas"] = 0.0
                #####################################
                if r[8] != "":
                    if int(r[8]) > 10:
                        dic["OrdinarioPracticas"] = float(r[8])/100
                    else:
                        dic["OrdinarioPracticas"] = float(r[8])
                else:
                    dic["OrdinarioPracticas"] = 0.0
                #####################################
                lista.append(dic)
    return lista
def notafinal(l):
    newlist = []
    l.reverse()
    for i in l:
        nota = 0.0
        if i["OrdinarioPracticas"] != 0.0 :
            nota += (i["OrdinarioPracticas"] * 0.4)
        else:
            nota += (i["Practicas"] * 0.4)
        if i["Ordinario2"] != 0.0 :
            nota += (i["Ordinario2"] * 0.3)
        else:
            nota += (i["Parcial2"] * 0.3)
        if i["Ordinario1"] != 0.0 :
            nota += (i["Ordinario1"] * 0.3)
        else:
            nota += (i["Parcial1"] * 0.3)
        i["NotaFinal"] = nota
        newlist.append(i)
    return newlist

def suspapro(l):
    a = []
    s = []
    for i in l:
        x = int(i["Asistencia"].replace("%",""))
        if i["NotaFinal"] >= 5:
            if i["Practicas"] >= 4:
                if i["Parcial2"] >= 4:
                    if i["Parcial1"] >= 4:
                        if x > 75:
                            a.append(i["Apellidos"])
        else:
            s.append(i["Apellidos"])
    print(f"Los aprobados son: {a}")
    print(f"Los suspensos son: {s}")


#print(notafinal(examenesyasist(file)))
suspapro((notafinal(examenesyasist(file))))