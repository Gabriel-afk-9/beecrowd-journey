crescente = []

valor1,valor2,valor3 = map(int,input().split())
crescente.extend([valor1,valor2,valor3])

original = list(crescente)

alterada = sorted(crescente)

for num in alterada:
    print(num)

print()

for nume in original:
    print(nume)