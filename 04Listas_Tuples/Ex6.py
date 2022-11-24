#https://aprendeconalf.es/docencia/python/ejercicios/listas-tuplas/
clases = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
suspensas = []
for i in range(len(clases)):
    nota = int(input(f"Qué nota has sacado en {clases[i]}: "))
    if nota < 5 :
        suspensas.append(clases[i])
print(f"Estas son las asigntaturas suspensas:")
print(suspensas)