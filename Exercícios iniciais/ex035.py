# Alistamento militar
from datetime import date
atual = date.today().year
nasc = int(input('Informe o ano de seu nascimento no formato aaaa:'))
idade =  atual - nasc
prazo = 18 - idade
print('Você possui {} anos.'.format(idade))
if idade < 18:
    print('Ainda faltam {} anos para que seu alistamento seja obrigatório.'.format(prazo))
elif idade > 18:
    prazo = idade - 18
    print('Você está {} anos atrasado. Aliste-se imediatamente!'.format(prazo))
else:
    print('Está na hora de se alistar! Procure o centro de recrutamento mais próximo.')
