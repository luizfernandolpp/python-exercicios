# Aprovado ou Reprovado? Um clássico!
n1 = float(input('Informe a primeira nota:'))
n2 = float(input('Informe a segunda nota:'))
media = (n1+n2)/2
if media >= 7.0:
    print('O aluno está aprovado com média {}.'.format(media))
elif media >= 5.0 or media < 7.0:
    print('O aluno possui média {} e está de recuperação.'.format(media))
else:
    print('O aluno está reprovado com média {}.'.format(media))

