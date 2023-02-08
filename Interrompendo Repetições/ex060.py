# Tabuada de vários números até o usuário escolher um número negativo
print('------ TABUADA ------')
while True:
    c = 0
    n = int(input('Você quer a tabuada de qual valor?'))
    if n < 0:
        print('Não há tabuada para um número negativo.')
        break
    else:
        while c <= 10:
            r = n * c
            print(f'{n} x {c} = {r}')
            c = c + 1
print('----- FIM ------')

