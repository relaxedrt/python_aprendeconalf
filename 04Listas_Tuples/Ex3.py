#https://aprendeconalf.es/docencia/python/ejercicios/listas-tuplas/
asignaturas = ["Matemáticas", "Física", "Química", "Historia" , "Lengua"]
notas = []
for i in range(len(asignaturas)):
    nota  = input(f"Que nota has sacado en {asignaturas[i]}: ")
    notas.append(nota)
for j in range(len(asignaturas)):
    print(f"En {asignaturas[j]} has sacado un {notas[j]}")