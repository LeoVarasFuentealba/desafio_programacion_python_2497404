def es_palidromo(texto):
    palindromo = False
    texto = texto.lower().replace(" ", "")

    revertido = texto[::-1]
    if texto == revertido:
        palindromo = True

    return palindromo

print(es_palidromo('ojo jo'))
print(es_palidromo('Alberto'))