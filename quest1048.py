salario = float(input())

if 0 <= salario <= 400.00:
    pobre = salario * 0.15
    aumento1 = salario + pobre
    print(f'Novo salario: {aumento1:.2f}')
    print(f'Reajuste ganho: {pobre:.2f}')
    print(f'Em percentual: 15 %')
    
elif 400.01 <= salario <= 800.00:
    medio = salario * 0.12
    aumento2 = salario + medio
    print(f'Novo salario: {aumento2:.2f}')
    print(f'Reajuste ganho: {medio:.2f}')
    print(f'Em percentual: 12 %')
    
elif 800.01 <= salario <= 1200.00:
    bom = salario * 0.10
    aumento3 = salario + bom
    print(f'Novo salario: {aumento3:.2f}')
    print(f'Reajuste ganho: {bom:.2f}')
    print(f'Em percentual: 10 %')
    
elif 1200.01 <= salario <= 2000.00:
    rico = salario * 0.07
    aumento4 = salario + rico
    print(f'Novo salario: {aumento4:.2f}')
    print(f'Reajuste ganho: {rico:.2f}')
    print(f'Em percentual: 7 %')
    
else:
    milionario = salario * 0.04
    aumento5 = salario + milionario
    print(f'Novo salario: {aumento5:.2f}')
    print(f'Reajuste ganho: {milionario:.2f}')
    print(f'Em percentual: 4 %')

