import copy

def altera_no_local(objeto, operacao):
    valor_antes = copy.deepcopy(objeto)
    operacao(objeto)
    return objeto != valor_antes


def altera_lista(lista):
    lista.append(4)


def altera_dict(dicionario):
    dicionario["idade"] = 17


def altera_set(conjunto):
    conjunto.add(4)


def altera_bytearray(dados):
    dados[0] = 100


def altera_string(texto):
    texto.upper()


def altera_tupla(tupla):
    tupla + (4,)


def altera_bytes(dados):
    dados + b"d"


def altera_frozenset(conjunto):
    conjunto.union({4})


print(altera_no_local([1, 2, 3], altera_lista))

print(altera_no_local({"nome": "Vitor"}, altera_dict))

print(altera_no_local({1, 2, 3}, altera_set))

print(altera_no_local(bytearray(b"abc"), altera_bytearray))

print(altera_no_local("abc", altera_string))

print(altera_no_local((1, 2, 3), altera_tupla))

print(altera_no_local(b"abc", altera_bytes))

print(altera_no_local(frozenset({1, 2, 3}), altera_frozenset))
