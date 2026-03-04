from fractions import Fraction

resultados = []
quantidade = int(input())

for _ in range(quantidade):
    expressao = input()
    partes = expressao.split()

    N1 = int(partes[0])
    D1 = int(partes[2])
    op = partes[3]
    N2 = int(partes[4])
    D2 = int(partes[6])

    if op == '+':
        num = N1*D2 + N2*D1
        deno = D1*D2
    elif op == '-':
        num = N1*D2 - N2*D1
        deno = D1*D2
    elif op == '*':
        num = N1*N2
        deno = D1*D2
    elif op == '/':
        num = N1*D2
        deno = N2*D1

    frac = Fraction(num,deno)
    simp_N = frac.numerator
    simp_D = frac.denominator

    if (simp_N == num) and (simp_D == deno):
        resultados.append(f'{num}/{deno} = {num}/{deno}')
    else:
        resultados.append(f'{num}/{deno} = {simp_N}/{simp_D}')

for resultado in resultados:
    print(resultado)