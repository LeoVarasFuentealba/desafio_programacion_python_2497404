def lista_plana(lista):

    lista_aplanada = []
    for i in lista:
        if type(i) is list:
            lista_aplanada.extend(i)
        else:
            lista_aplanada.append(i)
    
    return lista_aplanada

print(lista_plana([3,4,[1,5,3],1, 6, 4, [8,1,4,6]]))