#https://aprendeconalf.es/docencia/python/ejercicios/funciones/
def mcd(n, m):
    rest = 0
    while(m > 0):
        rest = m
        m = n % m
        n = rest
    return n
def mcm(n,m):
    if n > m:
        greater = n
    else:
        greater = m
    while (greater % n != 0) or (greater % m !=0):
        greater += 1
    return greater

print(mcd(24, 36))
print(mcm(24, 36))