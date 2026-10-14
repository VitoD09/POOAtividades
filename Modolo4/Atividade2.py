contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
print(contador)

def incrementar(valor):
    return valor + 1

contador = incrementar(0)
print(contador)
