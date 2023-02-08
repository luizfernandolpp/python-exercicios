# Programa com informações sobre texto inserido.
nome = str(input('Informe o seu nome completo:')).strip()
print('Seu nome em letras maiúsculas é: {}' .format(nome.upper()))
print('Seu nome em letras minúsculas é: {}' .format(nome.lower()))
print('Seu nome ao todo possui {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome possui {} letras'.format(nome.find(' ')))




