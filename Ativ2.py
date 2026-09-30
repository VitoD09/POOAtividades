def adicionar_tarefa(tarefa, lista=None):
    if lista is None:
        lista = []

    lista.append(tarefa)
    return lista


print(adicionar_tarefa.__defaults__)

print(adicionar_tarefa("estudar"))
print(adicionar_tarefa("revisar"))
print(adicionar_tarefa("praticar"))

print(adicionar_tarefa.__defaults__)
