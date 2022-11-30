#https://aprendeconalf.es/docencia/python/ejercicios/diccionarios/
name = input("Cual es tu nombre?: ")
age = (input("Cuantos años tienes?: "))
adress = input("Donde vives?: ")
tlf = (input("Cual es tu numero de telefono?: "))
info = {'name':name,'age':age, 'adress':adress,'tlf':tlf}
print(f"{info['name']} tiene {info['age']} años, vive en {info['adress']} y su número de telefono es {info['tlf']}.")
