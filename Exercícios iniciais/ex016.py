# Calculando a hipotenusa de triângulo retângulo.
from math import sqrt, pow
co = float(input('Informe o valor do cateto oposto:'))
ca = float(input('Informe o valor do cateto adjacente:'))
h = sqrt(pow(co, 2) + pow(ca, 2))
print('A hipotenusa deste triângulo retângulo é igual a {}'.format(h))
