A,B,C = map(float,input().split())

triangulo = B + C > A 

if A + B > C and C + B > A and A + C > B:
    perimetro = A + B + C
    print(f'Perimetro = {perimetro:.1f}')
else:
    area = (A + B) * C / 2
    print(f'Area = {area:.1f}')