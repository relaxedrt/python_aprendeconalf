#https://aprendeconalf.es/docencia/python/ejercicios/listas-tuplas/
clases = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
for i in range(0,len(clases)):
    nota = int(input(f"Qué nota has sacado en {clases[i]}: "))
    notas.append(nota)
for i in range(0,len(clases)):
    if notas[i]>=5:
        clases.pop(i)
        notas.pop(i)
print(f"Estas son las asigntaturas suspensas:")
print(clases)