def caracter_count(texto):
    texto = texto.lower().replace(" ", "")
    x = 0
    repeticiones = 0
    
    while x < len(texto) and repeticiones < 2:
        repeticiones = 0
        for caracter in texto:
            if caracter == texto[x]:
                repeticiones += 1
                if repeticiones > 1:
                    return caracter
        
        x += 1
    
    if repeticiones < 2: return 'None'

print(caracter_count("hola"))
print(caracter_count("hola mundo"))
