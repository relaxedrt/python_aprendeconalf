#https://aprendeconalf.es/docencia/python/ejercicios/listas-tuplas/
# listaraw = input("Dame una lista de numero separados por comas: ")
# listabien = listaraw.split(",")
# media = 0
# desvtip = 0
# sumatorio = 0
# for i in range(len(listabien)):
#     media += int(listabien[i])
# media = media / len(listabien)
# for k in range(len(listabien)):
#     sumatorio += float(listabien[k])*media
# desvtip = (sumatorio**2 / len(listabien))**(1/2)
# print(media)
# print(desvtip)
sample = input("Introduce una muestra de números separados por comas: ")
sample = sample.split(',')
n = len(sample)
for i in range(n):
    sample[i] = int(sample[i])
sample = tuple(sample)
sum = 0
sumsq = 0
for i in sample:
    sum += i
    sumsq += i**2
mean = sum/n
stdev = (sumsq/n-mean**2)**(1/2)
print('La media es', mean, ', y la desviación típica es', stdev)
