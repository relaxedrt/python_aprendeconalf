#https://aprendeconalf.es/docencia/python/ejercicios/depuracion/
base = input('Introduce la base imponible de la factura: ')

def aplica_iva(base, iva = 0.21):
    base += base * iva   
    return base 

print(aplica_iva(int(base)))