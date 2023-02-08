# MEGASENA!
from random import randint
from time import sleep
print("-" * 30)
print('     JOGA NA MEGA SENA     ')
print("-" * 30)
valores = [] # Lista com os valores a serem gerados de maneira aleatória.
n = int(input('Quantos jogos você deseja fazer? '))
print("=" * 5, end=' ')
print(f'SORTEANDO {n} JOGOS', end=' ')
print("=" * 5)
j = 1
while j <= n:
    for c in range(0, 6):  # Condição para gerar os valores da aposta de maneira aleatória.
        valores.append(randint(0, 60))
        valores.sort()
    print(f'Jogo {j}: {valores[:]}')
    valores.clear()
    j += 1
    sleep(0.8)
print("=" * 10, end=' ')
print('BOA SORTE!', end=' ')
print("=" * 10)



