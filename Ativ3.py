import copy

matriz = [[1, 2], [3, 4]]

rasa = copy.copy(matriz)
profunda = copy.deepcopy(matriz)

rasa[0][0] = 9

print(matriz)
print(rasa)

profunda[0][0] = 8

print(matriz)
print(profunda)
