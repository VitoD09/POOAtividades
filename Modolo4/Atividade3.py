def criar_contador(inicio):
    total = inicio

    def incrementar():
        nonlocal total
        total += 1
        return total

    return incrementar

a = criar_contador(0)
b = criar_contador(10)

print(a())
print(b())
