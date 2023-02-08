# Categoria de natação por idade
age = int(input('Informe a idade do atleta:'))
print('O atleta possui {} anos.'.format(age))
if age <= 9:
    print('O atleta deve disputar a categoria MIRIM.')
elif age > 9 and age <= 14:
    print('O atleta deve disputar a categoria INFANTIL.')
elif age > 14 and age <= 19:
    print('O atleta deve disputar a categoria JUNIOR.')
elif age > 19 and age <= 20:
    print('O atleta deve disputar a categoria SÊNIOR.')
else:
    print('O atleta deve disputar a categoria MASTER.')