quantidade = int(input())
for i in range(quantidade):
    a,b = map(int,input().split())
    try:
        soma = a / b
        print(soma)
    except ZeroDivisionError:
        print('divisao impossivel')
