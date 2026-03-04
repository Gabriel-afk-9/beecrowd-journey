num_val = []

while True:

    notas = float(input())
    if 0 <= notas <= 10:
        num_val.append(notas)

        if len(num_val) == 2:
            soma = sum(num_val)/2
            print(f'media = {soma:.2f}')
            break
    else:
        print("nota invalida")
