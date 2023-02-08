# Sequência de Fibonacci
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Informe quantos termos você deseja para a sequência de Fibonacci:'))
t1 = 0 # primeiro termo
t2 = 1 # segundo termo
c = 3 # contador começa em três porque os dois primeiros termos já estão especificados.
print('{} → {}'.format(t1, t2), end=' ')
while c <= n:
    t3 = t1 + t2
    print('→ {}'.format(t3), end=' ') # end=' ' evita a quebra de linha no comando print.
    t1 = t2
    t2 = t3
    c = c + 1
print('→ FIM')