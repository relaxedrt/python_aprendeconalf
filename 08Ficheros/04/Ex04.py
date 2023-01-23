#https://aprendeconalf.es/docencia/python/ejercicios/ficheros/
from urllib import request
from urllib.error import URLError
def checkurl(url):
    try:
        pagina = request.urlopen(url)
    except URLError:
        print(f"La url {url} no existe.")
        return None
    else:
        pagina.close()
        return url
def wordcounter(url):
    if url == None:
        return
    else:
        f = request.urlopen(url)
        data = f.read()
        return len(data.split())

print(wordcounter(checkurl('https://www.gutenberg.org/files/2000/2000-0.txt')))
print(wordcounter(checkurl('https://no-existe.txt')))