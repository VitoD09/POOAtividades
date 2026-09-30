import time

def concatenar_com_mais(quantidade):
    resultado = ""

    for i in range(quantidade):
        resultado += "abc"

    return resultado


def concatenar_com_join(quantidade):
    partes = []

    for i in range(quantidade):
        partes.append("abc")

    return "".join(partes)


inicio = time.perf_counter()
concatenar_com_mais(500000)
tempo_mais_500 = time.perf_counter() - inicio

inicio = time.perf_counter()
concatenar_com_mais(2000000)
tempo_mais_2000 = time.perf_counter() - inicio


inicio = time.perf_counter()
concatenar_com_join(500000)
tempo_join_500 = time.perf_counter() - inicio

inicio = time.perf_counter()
concatenar_com_join(2000000)
tempo_join_2000 = time.perf_counter() - inicio


print("+= 500000:", tempo_mais_500)
print("+= 2000000:", tempo_mais_2000)

print("join 500000:", tempo_join_500)
print("join 2000000:", tempo_join_2000)

print("Aumento do +=:", tempo_mais_2000 / tempo_mais_500)
print("Aumento do join:", tempo_join_2000 / tempo_join_500)
