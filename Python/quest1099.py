l =[]
v = []
a = int(input())

for i in range(a):
    valor,valor2 = map(int,input().split())
    l.append((valor,valor2))

for valor,valor2 in l:
     soma = 0
     for num in range(min(valor,valor2)+1,max(valor,valor2)):
         if num % 2 != 0:
            soma += num
            v.append(num)
     print(soma)