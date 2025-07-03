def num_traingular(fila):
    acomulador = 0
    for i in range(1, fila + 1):
        acomulador = acomulador + i

    return acomulador

print(num_traingular(3))
print(num_traingular(4))
