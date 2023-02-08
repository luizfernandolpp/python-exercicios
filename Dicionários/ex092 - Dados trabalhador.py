# Dados trabalhadores (RHuy)?
from datetime import date
dados = {}
nome = str(input('Informe o nome do funcionário: ')).strip()
nascimento = int(input('Informe o de nascimento (formato:AAAA): '))
idade = date.today().year - nascimento
ctps = int(input('Informe o número da CTPS (0 não possui): '))
if ctps != 0:
    anocontrato = int(input('Informe o ano da contratação (formato:AAAA): '))
    salario = float(input('Informe o salário do funcionário: '))

