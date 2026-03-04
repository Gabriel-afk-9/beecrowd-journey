d = []
f = 0
e = 0
x = int(input())
for i in range(x):
  x2 = int(input())
  d.append(x2)
  if 10 <= x2 <= 20:
    e += 1
  else:
    f += 1
print(f'{e} in')
print(f'{f} out')