#https://aprendeconalf.es/docencia/python/ejercicios/ficheros/
from urllib import request
url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true"
pais = input("Que país quieres investigar el PIB?: ")
def checkpib(p):
    f = request.urlopen(url)
    data = f.read()
    #linea = f.readlines()
    for linea in data:
        if p in linea:
            return linea
            
print(checkpib(pais))