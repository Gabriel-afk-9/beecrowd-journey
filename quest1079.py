l = []
m = int(input())

for i in range(m):
 x,y,z = map(float,input().split())
 resultado = (x*2 + y*3 + z*5) / (10)
 l.append(resultado)

for r in l:
 print(f'{r:.1f}')