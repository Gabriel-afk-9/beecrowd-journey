todos_numeros = []
pares = []
for i in range(5):
    valor = float(input())
    todos_numeros.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
print((len(pares)),f'valores positivos')