_, start_day = input().split()
start_day = int(start_day)

hours1, minutes1, seconds1 = map(int,input().split(' : '))

_, end_day = input().split()
end_day = int(end_day)

hours2, minutes2, seconds2 = map(int,input().split(' : '))

start_seconds = start_day * 86400 + hours1 * 3600 + minutes1 * 60 + seconds1
end_seconds = end_day * 86400 + hours2 * 3600 + minutes2 * 60 + seconds2

difference = end_seconds - start_seconds 

days = difference // 86400
difference %= 86400

hour = difference // 3600
difference %= 3600

minute = difference // 60
second = difference % 60

print(f'{days} dia(s)')
print(f'{hour} hora(s)')
print(f'{minute} minuto(s)')
print(f'{second} segundo(s)')