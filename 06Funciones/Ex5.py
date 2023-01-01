#https://aprendeconalf.es/docencia/python/ejercicios/funciones/
import math as m
radio = float(input("Cual es el radio del circulo?: "))
altura = float(input("Cual es la altura del cilindro?: "))
def sbase(r):
    s = m.pi * (r*r)
    return s
def vcil(s, h):
    print(s*h)
    return s*h
vcil(sbase(radio),altura)
