# nota1, nota2, nota3, nota4 = map(float,input().split())
# media = (nota1*2 + nota2*3 + nota3*4 + nota4*1)/10

# if media >= 7.0:
#     print(f'Media: {media:.1f}')
#     print('Aluno aprovado.')
# elif media < 5.0:
#     print(f'Media: {media:.1f}')
#     print('Aluno reprovado.')
# elif 5.0 <= media <= 6.9:
#     print(f'Media: {media:.1f}')
#     print('Aluno em exame.') 
    
#     notaEx = float(input())
#     print(f'Nota do exame: {notaEx:.1f}')
#     recalcular = (media + notaEx) / 2
#     if recalcular >= 5.0:
#         print('Aluno aprovado.')
#         print(f'Media final: {recalcular:.1f}')   
#     elif recalcular <= 4.9:
#         print('Aluno reprovado.')   
#         print(f'Media final: {recalcular:.1f}')   

def calcular_media(nota1,nota2,nota3,nota4):
    return (nota1*2 + nota2*3 + nota3*4 + nota4*1)/10

def verificar_situacao(media):
    if media >= 7.0:
        print(f'Media: {media:.1f}')
        print('Aluno aprovado.')
    elif media < 5.0:
        print(f'Media: {media:.1f}')
        print('Aluno reprovado.')
    elif 5.0 <= media <= 6.9:
        print(f'Media: {media:.1f}')
        print('Aluno em exame.')
        return 'exame'
    
def processar_exame(media):
    notaEx = float(input())
    print(f'Nota do exame: {notaEx:.1f}')
    recalcular = (media + notaEx) / 2
    if recalcular >= 5.0:
        print('Aluno aprovado.')
        print(f'Media final: {recalcular:.1f}')   
    elif recalcular <= 4.9:
        print('Aluno reprovado.')   
        print(f'Media final: {recalcular:.1f}')
        
def main():
    nota1, nota2, nota3, nota4 = map(float,input().split())
    
    media = calcular_media(nota1,nota2,nota3,nota4)
    
    situacao = verificar_situacao(media)
    
    if situacao == 'exame':
        processar_exame(media)
        
if __name__=='__main__':
    main()
    
    
    