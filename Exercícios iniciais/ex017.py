# Exercício para calcular seno, cosseno e tangente de um ângulo qualquer.
import math
x = float(input('Informe o ângulo em graus:'))
s = math.sin(math.radians(x))
c = math.cos(math.radians(x))
t = math.tan(math.radians(x))
print('O seno de {} é {} \n O cosseno de {} é {} \n A tangente de {} é {}'.format(x, s, x, c, x, t))

