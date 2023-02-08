# Quantidade de tinta necessária para pintar uma área sabendo que ela cobre 2m² por litro.
b = float(input('Insira a largura da parede em metros.'))
h = float(input('Insira a altura da parede em metros.'))
area = b*h
litro = area/2
print('Para pintar uma parede de {:0.2f}m² você precisará de {:0.2f} litros de tinta'.format(area, litro))

