# Analisador completo
somaidade = 0
maioridadehomem = 0
nomevelho = ''
numulheres = 0
for c in range(1, 5):
    print('------ {}ª PESSOA ------'.format(c))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip()
    somaidade = somaidade + idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        numulheres = numulheres + 1


media = somaidade / 4
print('A média de idade do grupo é de {:0.0f} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
if numulheres == 1:
    print('O grupo possui {} mulher com menos de 20 anos.'.format(numulheres))
else:
    print('O grupo possui {} mulheres com menos de 20 anos'.format(numulheres))
