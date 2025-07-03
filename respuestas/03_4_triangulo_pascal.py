def traingulo_pascal(num_listas):
    triangulo = []
    for i in range(num_listas):
        fila = []
        if i == 0:
            triangulo.append([1])
        else:
            fila_anterior = triangulo[i-1]
            for x in range(i + 1):
                if x == 0 or x == len(fila_anterior):
                    fila.append(1)
                else:  
                    for j in range(len(fila_anterior)):
                        if j == x:
                            fila.append(fila_anterior[j] + fila_anterior[j-1])
                    
            triangulo.append(fila)
    return triangulo

print(traingulo_pascal(20))
