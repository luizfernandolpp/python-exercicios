# tuplas bagunça

tupla = (int(input('Insira um valor:')),int(input('Insira um valor:')),int(input('Insira um valor:')),int(input('Insira um valor:')))
print(f'Você digitou os seguintes valores: {tupla}')
nove = 0
pos = 0
for c in tupla:
    if c == 9:
        nove += 1
    else:
        nove = 0
if nove != 0:
    print(f'O número 9 aparece {nove} vezes.')
else:
    print(f'O número 9 não aparece nenhuma vez.')



