start,end = map(int,input().split())

if start < end:
    duration =  end - start
elif start >= end:
    duration = (24 - start) + end

print(f'O JOGO DUROU {duration} HORA(S)')
