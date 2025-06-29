todos_numeros = []
pares = []
positivo = []
negativo = []
impar = []
for i in range(5):
    valor = int(input())
    todos_numeros.append(valor)
    
    if valor % 2 == 0:
     pares.append(valor)
    else:
     impar.append(valor)

        
    if valor > 0:
     positivo.append(valor)
    elif valor < 0:
     negativo.append(valor)

    
print(len(pares),'valor(es) par(es)')
print(len(impar),'valor(es) impar(es)')
print(len(positivo),'valor(es) positivo(s)')
print(len(negativo),'valor(es) negativo(s)')