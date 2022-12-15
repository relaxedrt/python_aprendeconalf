#https://aprendeconalf.es/docencia/python/ejercicios/diccionarios/
credits = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
# mate = 'Matemáticas'
# fisica = 'Física'
# quimica = 'Química'
# if mate in credits:
#     print(f'{mate} tiene {credits["Matemáticas"]} creditos.')
# if fisica in credits:
#     print(f'{fisica} tiene {credits["Física"]} creditos.')
# if quimica in credits:
#     print(f'{quimica} tiene {credits["Química"]} creditos.')
#--------------------------------------------------------
#Solucion buena y eficiente.
for asignatura, creditos in credits.items():
    print(f"{asignatura} tiene {creditos} creditos")