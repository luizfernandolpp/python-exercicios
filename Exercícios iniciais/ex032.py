# As três retas podem formar um triângulo?
# desigualdade triangular: a soma de dois lados de um triângulo deve ser sempre maior que o terceiro lado.
r1 = float(input('Informe o comprimento da primeira reta:'))
r2 = float(input('Informe o comprimento da segunda reta:'))
r3 = float(input('Informe o comprimento da terceira reta:'))
soma1 = r1 + r2
soma2 = r2 + r3
soma3 = r1 + r3
if soma1 > r3 and soma2 > r1 and soma3 > r2:
    print('Estas três retas podem formar um triângulo!')
else:
    print('Estas três retas não podem formar um triângulo!')


