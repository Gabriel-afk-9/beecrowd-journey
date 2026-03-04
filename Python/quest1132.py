a = int(input())
b = int(input())

if a > b:
   a,b = b,a

soma = 0
for x in range(a,b + 1):
    if x % 13 != 0:
     soma += x
print(soma)