#https://aprendeconalf.es/docencia/python/ejercicios/ficheros/
import tkinter
import customtkinter as tk

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

app = tk.CTk()
app.geometry("300x480")
app.title("Listin telefonico")

file = "00CustomTKinter/app/listin.txt"
def checkexist():
    try:
        f = open(file, "r")
        f.close()
    except FileNotFoundError:
        f = open(file,"a")
        f.write("LISTIN TELEFONICO \n")
def consult(nombre):
    f = open(file, "r")
    lineas = f.readlines()
    for l in lineas:
        if str(nombre) in l:
            return l
def newnum(nombre, numero):
    checkexist()
    f = open(file, "a")
    f.write(f"{nombre},{numero}\n")
    f.close()
def deletenum(nombre):
    f = open(file, "r")
    lineas = f.readlines()
    f.close()
    for l in lineas:
        if str(nombre) in l:
            lineas.remove(l)
    a = open(file, "w")
    for i in lineas:
        a.write(i)
def consultar():
    print(name)
    consult(name)
def newnumero():
    newnum(name, numb)
def deletenumero():
    newnum(name)
#TEXTOS INDICADORES
textbox1 = tk.CTkLabel(master=app, text="Nombre")
textbox1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

textbox2 = tk.CTkLabel(master=app, text="Numero")
textbox2.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
#INPUTS
nombre = tk.CTkEntry(master=app,
                    width=120,
                    height=25,
                    corner_radius=10)
nombre.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
name = nombre.get()

numero = tk.CTkEntry(master=app,
                    width=120,
                    height=25,
                    corner_radius=10)
numero.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
numb = numero.get()

#BOTONES
checkeo = tk.CTkButton(master = app, text="Comprobar existencia Listin", command = checkexist)
checkeo.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

consulta = tk.CTkButton(master = app, text="Consultar numero con nombre", command = consultar)
consulta.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

nuevonumero = tk.CTkButton(master = app, text="Agregar numero", command = newnumero)
nuevonumero.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

borrarnumero = tk.CTkButton(master = app, text="Borrar numero", command = deletenumero)
borrarnumero.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

#EJECUTAR APLICACION
app.mainloop()