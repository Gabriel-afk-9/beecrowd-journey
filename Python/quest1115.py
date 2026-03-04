l = []

while True:
    a,b = map(int,input().split())

    if a > 0 and b > 0:
        print('primeiro')
    elif a < 0 and b > 0:
        print('segundo')
    elif a < b and b < 0:
        print('terceiro')
    elif a > 0 and b < 0:
        print('quarto')
    if a == 0 or b == 0:
        break

