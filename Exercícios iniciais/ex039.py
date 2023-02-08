# Cálculo de IMC simples
peso = float(input('Informe o seu peso em quilogramas:'))
altura = float(input('Informe a sua altura em metros:'))
print('Você pesa {} quilos e possui {} metros de altura.'.format(peso,altura))
imc = peso/(altura**2)
print('Seu IMC é {:0.2f} kg/m²'.format(imc))
if imc < 18.5:
    print('Resultado: Abaixo do peso.')
elif imc >= 18.5 and imc < 25.0:
    print('Resultado: Peso ideal.')
elif imc >= 25 and imc < 30.0:
    print('Resultado: Sobrepeso.')
elif imc >= 30.0 and imc < 40:
    print('Resultado: Obesidade.')
else:
    print('Resultado: Obesidade mórbida.')