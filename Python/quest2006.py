def contar(T,respostas):
    return respostas.count(T)
    
T = int(input())
respostas = list(map(int,input().split()))
print(contar(T,respostas))