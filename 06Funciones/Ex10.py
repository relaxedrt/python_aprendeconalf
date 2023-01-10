#https://aprendeconalf.es/docencia/python/ejercicios/funciones/
def dectobin(num):
    bin = []
    while num > 0:
        bin.append(str(num % 2))
        num //= 2
        bin.reverse()
    return "".join(bin)

def bintodec(num):
    num = list(num)
    num.reverse()
    dec = 0
    for i in range(len(num)):
        dec += int(num[i]) * 2 **i
    return dec

print(dectobin(22))
print(bintodec("10110"))
