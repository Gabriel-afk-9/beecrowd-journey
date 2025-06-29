l = []
k = []
adicionado = 4
for x in range(7,4,-1):
    l.append(x)
for x in range(x + adicionado,6,-1):
   l.append(x)
for x in range(x + adicionado,8,-1):
   l.append(x)
for x in range(x + adicionado,10,-1):
   l.append(x)
for x in range(x + adicionado,12,-1):
   l.append(x)

for i in range(1,10,2):
    for _ in range(3):
     k.append(i)

for i in range(len(l)):
    print(f"I={k[i]} J={l[i]}")