#https://aprendeconalf.es/docencia/python/ejercicios/diccionarios/
#input = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
database = {}
userin = str(input("Introduce la cadena de texto de los clientes."))
clients = userin.split("\\n")
for i in clients:
    x = i.split(";")
    y = {
        "name" : x[1],
    "mail" : x[2],
    "tlf" : x[3],
    "discount" : x[4],
    }
    database[x[0]] = y
database.pop("nif")
print(database)