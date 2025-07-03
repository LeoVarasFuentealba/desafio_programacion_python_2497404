def get_duplicados(list):
    list_duplicated = []
    for i in list:
        contador = 0
        for x in range(len(list)):
            if i == list[x]:
                contador += 1
                if contador > 1 and i not in list_duplicated:
                    list_duplicated.append(i)
    
    return list_duplicated

print(get_duplicados([1,2,4,1,5,2,7,3,9,0,5,4]))