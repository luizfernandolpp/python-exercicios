# Jogo de par ou ímpar
from random import randint
from time import sleep
print('=-'*15)
print('JOGO DE PAR OU ÍMPAR')
print('=-'*15)
vitorias = 0
while True:
    escolha = str(input('Par ou Ímpar? [P/I]:')).strip().upper()
    if escolha  == "P":
        print('Ok! Eu sou ÍMPAR então...')
        sleep(1)
        print('Prepare-se para escolher seu número...')
        sleep(1)
        print('3...')
        sleep(1)
        print('2...')
        sleep(1)
        print('1...')
        pc = randint(0,5)
        jogador = int(input('Escolha seu número.'))
        soma = pc + jogador
        if soma % 2 == 0:
            print(f'Eu escolhi {pc} e você escolheu {jogador}. Somando dá {soma} que é PAR. Você venceu a rodada!')
            print('-'*30)
            vitorias = vitorias + 1
        else:
            print(f'Eu escolhi {pc} e você escolheu {jogador}. Somando dá {soma} que é ÍMPAR!')
            print('=-'*24)
            break
    elif escolha == "I":
        print('OK! Eu sou PAR então...')
        sleep(1)
        print('Prepare-se para escolher seu número...')
        sleep(1)
        print('3...')
        sleep(1)
        print('2...')
        sleep(1)
        print('1...')
        pc = randint(0,5)
        jogador = int(input('Escolha seu número.'))
        soma = pc + jogador
        if soma % 2 == 0:
            print(f'Eu escolhi {pc} e você escolheu {jogador}. Somando dá {soma} que é PAR!')
            print('=-'*24)
            break
        else:
            print(f'Eu escolhi {pc} e você escolheu {jogador}. Somando dá {soma} que é ÍMPAR. Você venceu a rodada!')
            print('-'*30)
            vitorias = vitorias + 1

    else:
        print("Entrada inválida! Por favor, escolha somente entre par ou ímpar [P/I].")

if vitorias == 0:
    print(f'FIM DE JOGO! Você não venceu nenhuma vez.')
elif vitorias == 1:
    print(f'FIM DE JOGO! Você venceu {vitorias} vez.')
else:
    print(f'FIM DE JOGO! Você venceu {vitorias} vezes.')
print('=-'*24)