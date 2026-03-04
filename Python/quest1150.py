x = int(input())

while True:
    z = int(input())
    if z > x:
        break
    
soma = x
cont = 1

while soma <= z:
    x += 1
    soma += x
    cont += 1

print(cont)