# Calculadora de pagamentos.
from time import sleep

valor = float(input('Informe o valor do produto:'))
print('As opções de pagamento são:')
print('À vista dinheiro\cheque com 10% de desconto. Para selecionar esta forma de pagamento digite 1.')
print('À vista no cartão com 5% de desconto. Para selecionar esta forma de pagamento digite 2.')
print('Parcelado em 2x sem juros no cartão. Para selecionar esta forma de pagamento digite 3.')
print('Parcelado em 3x ou mais com juros de 20% no cartão. Para selecionar esta forma de pagamento digite 4.')
forma = int(input('Escolha a forma de pagamento desejada:'))


if forma == 1:
    price = valor - valor * 0.10
    print('O produto sairá de R${:0.2f} por R${:0.2f}.'.format(valor, price))
elif forma == 2:
    price = valor - valor * 0.05
    print('O produto sairá de R${:0.2f} por R${:0.2f}.'.format(valor, price))
elif forma == 3:
    price = valor / 2
    print('O produto sairá a 2x de R${:0.2f}.'.format(price))
elif forma == 4:
    num = int(input('Informe em quantas vezes deseja parcelar:'))
    price = (valor + 0.20 * valor) / num
    print('O produto sairá a {} parcelas de R${:0.2f}.'.format(num, price))
