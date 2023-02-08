# Multa para excesso de velocidade acima de 80km/h:
v = float(input('Informe a velocidade do automóvel:'))
if v > 80.0:
    multa = (v - 80.0)*7
    print('Você ultrapassou o limite de velocidade e receberá uma multa por isso.')
    print('Sua multa custará R${:0.2f}'.format(multa))
else:
    print('Este veículo não foi multado.')

