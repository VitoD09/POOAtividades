funcoes = []

for i in range(3):
    def mostrar(valor=i):
        return valor
    funcoes.append(mostrar)

for f in funcoes:
    print(f())
