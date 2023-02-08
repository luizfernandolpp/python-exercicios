# JOKENPÔ!
import random
from time import sleep
print('Que tal uma partida de Jokenpô?')
sleep(0.5)
question = str(input('Você sabe como jogar?')).strip().upper()
if question == "NÃO" or question == "NAO" or question == "N":
    print('Funciona assim: quando eu disser "Pô!", nós escolhemos uma opção entre pedra, papel e tesoura.')
    print('Pedra vence tesoura. Tesoura vence papel. Papel vence pedra. O resto dá empate.')
    sleep(5)
    question = str(input('E aí, pronto para jogar?')).strip().upper()
    if question == "SIM" or question == "S":
        print('ÓTIMO! Vamos começar então!')
else:
    print('ÓTIMO! Vamos começar então!')
sleep(2)
computador = ['Pedra', 'Papel', 'Tesoura']
pc = random.choice(computador)
print('Jo...')
sleep(1)
print('Ken...')
sleep(1)
print('Pô!')
print(pc)