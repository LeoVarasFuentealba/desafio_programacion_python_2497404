def es_numero_primo(num):
    if num != 1:
        for i in range (2, num):
            if num % i != 0:
                return True
            else:
                return False
    else:
        return False

print(es_numero_primo(3)) # True
print(es_numero_primo(12)) # False
print(es_numero_primo(43)) # True
    