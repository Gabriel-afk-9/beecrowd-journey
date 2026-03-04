valores = {1:4.00,
           2:4.50,
           3:5.00,
           4:2.00,
           5:1.50}
itens,vezes = input().split()

itens = int(itens)
vezes = int(vezes)

if itens in valores :
        valor = valores[itens]
        resultado = valor * vezes
        print(f'Total: R$ {resultado:.2f}')

