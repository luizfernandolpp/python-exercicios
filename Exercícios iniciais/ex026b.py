# Exercício que mostra o primeiro e o último nome de uma pessoa (código alternativo):
n = str(input('Informe o seu nome completo:')).strip().title()
nome = n.split()
print(nome)
print('O seu primeiro nome é {}'.format(nome[0]))
print('O seu último nome é {}'.format(nome[len(nome)-1]))
