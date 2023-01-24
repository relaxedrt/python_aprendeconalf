#https://aprendeconalf.es/docencia/python/ejercicios/ficheros/
from urllib import request
url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true"
pais = input("Que país quieres investigar el PIB?: ")
def checkpib(p):
    f = request.urlopen(url)
    lineas = f.readlines()
    for l in lineas:
        if p in str(l):
            return f"{str(lineas[0])}\n{l}"
print(checkpib(pais))