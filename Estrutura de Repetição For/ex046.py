# Soma de pares apenas
soma = 0
for c in range(0,6):
    n = int(input('Escolha um número inteiro:'))
    if n % 2 == 0:
        soma = soma + n
print('A soma de todos os números pares escolhidos é {}.'.format(soma))

