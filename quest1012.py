import math

A,B,C = map(float,input().split())
math.pi=3.14159

triangulo = A*C/2
circulo = math.pi*C**2
trapezio = (A+B) * C/2
quadrado = B**2
retangulo = A*B

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')