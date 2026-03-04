hi, mi, hf, mf = map(int, input().split())

total_minutos_inicio = hi*60 + mi
total_minutos_fim = hf*60 + mf

if total_minutos_inicio < total_minutos_fim:
    duracao = total_minutos_fim - total_minutos_inicio
else:
    duracao = (60*24 - total_minutos_inicio) + total_minutos_fim

total_duracao_horas = duracao // 60
total_duracao_minutos = duracao % 60

print(f'O JOGO DUROU {total_duracao_horas} HORA(S) E {total_duracao_minutos} MINUTO(S)')