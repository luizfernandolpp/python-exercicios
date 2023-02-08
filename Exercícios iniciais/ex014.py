# Total a pagar em aluguel de carro por dia e km rodado.
km = float(input('Informe a quantidade de quilômetros rodados:'))
dia = int(input('Informe o número de dias em que o carro esteve alugado:'))
preco = 60*dia + 0.15*km
print('O automóvel percorreu {} km ao longo de {} dias. O preço total será de R${:0.2f}'.format(km, dia, preco))
