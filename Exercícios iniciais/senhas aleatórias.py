# Gerando senhas aleatórias
import random
lower = "abcdfeghijklmnopqrstuvwxyz"
upper = "ABCDFEGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%&*().\/_-"

string = lower + upper + numbers + symbols
lenght = 12
password = "".join(random.sample(string,lenght))

print('Your password is: {}'.format(password))