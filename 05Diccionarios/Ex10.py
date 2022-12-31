#https://aprendeconalf.es/docencia/python/ejercicios/diccionarios/
database = {}
option = int(input("(1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. "))
while option != 6:
    if option == 1:
        dni = int(input("Cual es el dni del cliente: "))
        name = input("Cual es el nombre del cliente: ")
        address = input("Cual es la direccion del cliente: ")
        tlf = input("Cual es el telefono del cliente: ")
        mail = input("Cual es el mail del cliente: ")
        pref = input("Es un cliente preferente?: ")
        userinfo = {"name":name,
        "address":address,
        "tlf":tlf,
        "mail":mail,
        "pref":pref}
        database[dni] = userinfo
        print(database)
        option = int(input("(1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. "))
    if option == 2:
        dni = input("Cual es el dni del cliente que deseas borrar?: ")
        database.pop(dni)
        print("Esta es la base de datos actualizada: ")
        print(database)
        option = int(input("(1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. "))
    if option == 3:
        dni = input("Cual es el dni del cliente: ")
        print(database[dni])
        option = int(input("(1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. "))
    if option == 4:
        print(database)
        option = int(input("(1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. "))
    if option == 5:
        for clave, valor in database.items():
            if valor['pref']:
                print(clave, valor['name'])
        option = int(input("(1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. "))
        
