A,B,C = map(float,input().split())

delta = B**2 - 4*A*C

if delta < 0 or A == 0:
    print('Impossivel calcular')
else:
    calcular = delta **0.5
    x1 = (-B + calcular) / (2*A)
    x2 = (-B - calcular) / (2*A)
    print(f"R1 = {x1:.5f}\nR2 = {x2:.5f}")