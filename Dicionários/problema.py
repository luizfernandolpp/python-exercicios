# Problema da Lápide (?)
e = int(input('Informe um número'))
c = 3   # argumento da primeira raiz (que será quadrada)
n = 1   # definirá a potência de 2 das raizes internas
R = 1   # Função resposta inicial que será multiplicada pela função r
while c <= e:
    r = c ** (1 / (2 ** n))   # função que executa o cálculo das raizes
    R *= r  # R se torna a função r
    c += 1
    n += 1
    r *= r  # r é multiplicada pelo valor seguinte

print(f'O resultado é {R:.50f}')
