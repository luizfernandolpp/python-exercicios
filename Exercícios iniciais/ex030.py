# Uma viagem pode custar caro:
d = float(input('Informe a distância da viagem em Km:'))
if d <= 200:
    preco = 0.50*d
    print('Esta viagem custará R${:0.2f}'.format(preco))
else:
    preco = 0.45*d
    print('Esta viagem custará R${:0.2f}'.format(preco))
