values = []
positive = []

for i in range(6):
    value = float(input())
    values.append(value)

for val in values:
    if val > 0:
        positive.append(val)

average = sum(positive)/len(positive)

print(len(positive),'valores positivos')
print(f'{average:.1f}')