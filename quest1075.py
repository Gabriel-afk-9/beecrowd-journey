l = []

for i in range(100):
    a = int(input())
    l.append(a)

larger = max(l)
position = l.index(larger)

print(larger)
print(position + 1)
