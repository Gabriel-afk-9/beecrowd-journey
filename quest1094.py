n = int(input())
c = []
r = []
s = []

for i in range(n):
    tipoAnimal = input().upper()
    partes = tipoAnimal.split()
    
    if len(partes) == 2:
        number = int(partes[0])
        tipo = partes[1]
        
        if tipo == 'C':
            c.append(number)
            
        elif tipo == 'R':
            r.append(number)
            
        elif tipo == 'S':
            s.append(number)

coelho = sum(c)
rato = sum(r)
sapo = sum(s)
cobaiasTotal = rato + sapo + coelho

cPercentual = (coelho / cobaiasTotal) * 100
rPercentual = (rato / cobaiasTotal) * 100
sPercentual = (sapo / cobaiasTotal) * 100

print(f'Total: {cobaiasTotal} cobaias')
print(f'Total de coelhos: {coelho}')
print(f'Total de ratos: {rato}')
print(f'Total de sapos: {sapo}')
print(f'Percentual de coelhos: {cPercentual:.2f} %')
print(f'Percentual de ratos: {rPercentual:.2f} %')
print(f'Percentual de sapos: {sPercentual:.2f} %')
    
