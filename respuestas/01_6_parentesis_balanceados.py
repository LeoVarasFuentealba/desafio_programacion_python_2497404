def parentesis_balanceado(text):
    der = 0
    izq = 0
    for caracter in text:
        if caracter == ')':
            der += 1
        elif caracter == '(':
            izq += 1
    
    return der == izq

print (parentesis_balanceado("hola (no) entiendo ( que si())"))