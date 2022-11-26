#https://aprendeconalf.es/docencia/python/ejercicios/listas-tuplas/
v1 =  [1,2,3]
v2 = [-1,0,2]
res = 0
for i in range(0,len(v1)):
    res =  res + (v1[i]*v2[i])
print(res)