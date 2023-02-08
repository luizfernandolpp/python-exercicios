# Exercício que mostra o primeiro e o último nome de uma pessoa (meu código):
nome = str(input('Insira seu nome completo:')).strip().title()
print('O seu primeiro nome é {}'.format(nome[:nome.find(' ')]))
print('O seu último nome é {}'.format(nome[nome.rfind(' ')+1:]))





