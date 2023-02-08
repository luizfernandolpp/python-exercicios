# Programa de adivinhação:
from random import randint # Import para aleatoriedade
from time import sleep # Import para fazer o programa pausar momentaneamente.
computador = randint(0,5) # O computador irá 'pensar'.
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
jogador = int(input('Em qual número eu pensei?')) # O jogador escolhe um número.
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você me venceu!'.format(computador))
else:
    print('AHA, EU VENCI! Pensei em {} em vez de {}'.format(computador, jogador))




