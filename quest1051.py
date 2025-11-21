value = float(input())

if value <= 2000.00:
    print('Isento')
    
elif value <= 3000.00:
    result =  (value - 2000.00) * 0.08
    print(f'R$ {result:.2f}')
    
elif value <= 4500.00:
    result= (1000.00 * 0.08) + ((value - 3000.00)*0.18)
    print(f'R$ {result:.2f}')
    
else:
    result = (1000.00 * 0.08) + (1500.00 * 0.18) + ((value - 4500.00)*0.28) 
    print(f'R$ {result:.2f}')
