#https://aprendeconalf.es/docencia/python/ejercicios/diccionarios/
meses = {1:'enero',2:'febrero',3:'marzo',4:'abril',5:'mayo',6:'junio',7:'julio',8:'agosto',9:'septiembre',10:'octubre',11:'noviembre',12:'diciembre',}
fecha = input("Cual es tu fecha de nacimiento en este formato? dd/mm/aaaa: ")
lisfecha = fecha.split("/")
print(f"{lisfecha[0]} de {meses[int(lisfecha[1])]} de {lisfecha[2]}")