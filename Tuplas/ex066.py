# Brasileirão 2022
print("="*60)
print('CLASSIFICADOS PARA FASE DE GRUPOS DA LIBERTADORES 2023')
print("="*60)
colocados = ('Palmeiras','Internacional','Fluminense','Corinthians','Flamengo','Athletico','Atlético-MG','Fortaleza','São Paulo','América-MG','Botafogo','Santos','Goiás','Bragantino','Coritiba','Cuiabá','Ceará','Atlético-GO','Avaí','Juventude')
p = 0
for libertadores in colocados[0:5]: # 5 primeiros
    p += 1
    print(f'{p}.{libertadores}')

print("="*30)
print('REBAIXADOS P/ SÉRIE B 2023')
print("="*30)
p = 16
for rebaixados in colocados[16:20]:
    p += 1
    print(f'{p}.{rebaixados}')

print("="*30)
print('TIMES EM ORDEM ALFABÉTICA')
print("="*30)
print(sorted(colocados))


print("="*40)
print("POSIÇÃO NA TABELA DO TIME ESCOLHIDO")
print("="*40)
time = str(input('Escolha um time:')).strip().capitalize()
pos = colocados.index(time) + 1
print(f'{time} está na {pos}ª posição.')