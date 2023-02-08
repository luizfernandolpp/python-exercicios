# Emprestimo para comprar uma casa
from time import sleep
valor = float(input('Informe o valor da casa:'))
salario = float(input('Informe a sua renda:'))
anos = int(input('Informe o tempo em anos de financiamento:'))
print('Um momento enquanto analisamos a disponibilidade para o empréstimo...')
sleep(3)
mensal = 12*anos # tempo de financiamento convertido para meses
prestacao = valor/mensal # valor a ser pago por mês ao longo do financiamento.

if prestacao > salario*0.30:
    print('Desculpe, mas o empréstimo não pode ser efetuado.')
else:
    print('Empréstimo aprovado! O valor a ser pago mensalmente será de R${:0.2f}'.format(prestacao))





