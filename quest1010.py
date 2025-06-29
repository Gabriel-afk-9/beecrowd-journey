entrada1 = input().split()

a = int(entrada1[0])
b = int(entrada1[1])
c=float(entrada1[2])

entrada2 = input().split()

d=int(entrada2[0])
e=int(entrada2[1])
f=float(entrada2[2])

soma1=b*c
soma2=e*f
soma3=soma1+soma2
print(f'VALOR A PAGAR: R$ {soma3:.2f}')
