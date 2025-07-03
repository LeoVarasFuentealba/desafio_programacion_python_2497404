def lista_ordenada(list):
    ordenada = False
    while ordenada == False:
        x = 0
        cambios = 0
        for i in list:
            if x < len(list) -1:
                if i > list[x + 1]:
                    save = list[x]
                    list[x] = list[x + 1]
                    list[x + 1] = save
                    cambios += 1
            x += 1
        
        if cambios == 0:
            ordenada = True
            
    return list
                
print(lista_ordenada([1,5,4,1,8,2,3]))