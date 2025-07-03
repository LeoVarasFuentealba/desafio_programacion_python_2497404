def es_anagrama(texto1, texto2):
    list_text1 = sorted(texto1.upper())
    list_text2 = sorted(texto2.upper())

    return list_text1 == list_text2

print(es_anagrama('oojo', 'oooj'))