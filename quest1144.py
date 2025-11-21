valor = int(input())

for i in range(1,valor*2):
    if i <= valor:
     print(f'{i} {i*i} {i*i*i}')
     print(f'{i} {i*i+1} {i*i*i+1}')