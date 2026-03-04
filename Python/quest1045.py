a,b,c = map(float,input().split())

decreasing = sorted([a,b,c], reverse=True)
a,b,c = decreasing

if a >= b + c: 
    print('NAO FORMA TRIANGULO')
else:
    if  a**2 == b**2 + c**2:
        print('TRIANGULO RETANGULO')
    elif a**2 > b**2 + c**2:
        print('TRIANGULO OBTUSANGULO')
    elif a**2 < b**2 + c**2:
        print('TRIANGULO ACUTANGULO')

    if b == a == c:
        print('TRIANGULO EQUILATERO')
    elif b == a or b ==c or a == c:
        print('TRIANGULO ISOSCELES')
