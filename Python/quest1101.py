while True:
    m,n = map(int, input().split()) 
    
    if m <= 0 or n <= 0:
        break
    
    start = min(m, n)
    end = max(m, n)
    
    sequencia = list(range(start, end + 1))
    
    total = sum(sequencia)
    
    print(" ".join(map(str, sequencia)),f'Sum={total}')