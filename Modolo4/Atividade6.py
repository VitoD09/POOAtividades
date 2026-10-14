def criar_acumulador():
    total = 0

    def adicionar(valor):
        nonlocal total
        total += valor
        return total

    def zerar():
        nonlocal total
        total = 0

    return adicionar, zerar

adicionar, zerar = criar_acumulador()

adicionar(10)
zerar()
print(adicionar(5))
