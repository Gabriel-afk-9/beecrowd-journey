l = []
while True:
    a = int(input())
    if a < 0:
        break
    l.append(a)
    soma = sum(l)/len(l)
print(f'{soma:.2f}')