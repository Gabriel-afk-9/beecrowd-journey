x = int(input())
y = int(input())

start = min(x,y)
end = max(x,y)

l = []

for i in range(start + 1, end):
    if i % 5 == 2 or i % 5 == 3:
        result = i
        l.append(result)
        
for j in l:
    print(j)
    