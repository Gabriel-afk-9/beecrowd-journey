segundos = int(input())
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos2 = segundos % 60

print(f'{horas}:{minutos}:{segundos2}')