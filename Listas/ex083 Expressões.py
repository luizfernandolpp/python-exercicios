# Validando expressões matemáticas por parênteses
expressao = str(input('Digite a expressão:'))
pilha = []
for simb in expressao:
    if simb == "(":
        pilha.append("(")
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
    