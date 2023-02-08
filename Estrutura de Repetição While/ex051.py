# Jogo de Adivinhação 2.0
from random import randint
from time import sleep
print('------ JOGO DA ADIVINHAÇÃO ------')
print('Vamos jogar um jogo?')
print('Eu vou pensar em um número entre 0 e 10 e você terá que adivinhar em qual eu pensei.')
print('Deixe-me pensar...')
pc = randint(0, 10)
sleep(3)
palpites = 0
jogador = int(input('Em qual número eu pensei?'))
print('PROCESSANDO...')
sleep(1)
while jogador != pc:
    print('AHA! Eu venci! Pensei no número {} em vez do número {}. Tente de novo!'.format(pc, jogador))
    pc = randint(0, 10)
    jogador = int(input('Em qual número eu pensei?'))
    print('PROCESSANDO...')
    sleep(1)
    palpites = palpites + 1

print('Parabéns! Eu realmente pensei no número {}. Você venceu em {} tentativas.'.format(jogador, palpites))
print('------ FIM ------')