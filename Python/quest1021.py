valor = float(input())
valor_cent = int(round(valor * 100))

cedulas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [ 100, 50, 25, 10, 5, 1]
print('NOTAS:')
for cedula in cedulas:
    qnt = valor_cent // cedula
    valor_cent %= cedula
    print(f'{qnt:.0f} nota(s) de R$ {cedula // 100}.00')

print('MOEDAS:')
for moeda in moedas:
    qntm = valor_cent // moeda
    valor_cent %= moeda
    print(f'{qntm:.0f} moeda(s) de R$ {moeda / 100:.2f}')
