indentificar1 = input()
indentificar2 = input()
indentificar3 = input()

if indentificar1 == 'vertebrado':
    if indentificar2 == 'ave':
        if indentificar3 == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    if indentificar2 == 'mamifero':
        if indentificar3 == 'onivoro':
            print('homem')
        else:
            print('vaca')
if indentificar1 == 'invertebrado':
    if indentificar2 == 'inseto':
        if indentificar3 == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    if indentificar2 == 'anelideo':
        if indentificar3 == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')        