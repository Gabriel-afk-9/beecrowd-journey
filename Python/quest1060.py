todos_numeros = []
positivo = []
for i in range(6):
    valor = float(input())
    todos_numeros.append(valor)
    if valor >= 0:
        positivo.append(valor)
print((len(positivo)),f'valores positivos')
