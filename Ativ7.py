No codigo Inicial a leituras foi alterada porque remove() está removendo os valores da lista original

def remover_negativos(numeros):
    resultado = []

    for numero in numeros:
        if numero >= 0:
            resultado.append(numero)

    return resultado


leituras = [12, -3, 7, -1, 5]

positivas = remover_negativos(leituras)

print(positivas)
print(leituras)
