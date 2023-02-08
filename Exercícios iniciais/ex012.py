# Exercício que mostra o salário de um funcionário com aumento de 15%.
n = float(input('Insira o salário atual.'))
aumento = n + 0.15*n
print('Com o aumento, o salário de R${:0.2f} passará a ser de R${:0.2f}'.format(n, aumento))
