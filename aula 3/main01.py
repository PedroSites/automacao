# Estrutura de repetição For
# Utilizada para repetir um conjunto de instruções por un num determinando as vezes

# range(5): 0, 1, 2, 3, 4
# o ultimo numero nao entra

# range(valor inicial, valor final, passo)
# range(1,5,1): 1, 2, 3, 4
# range(4, 9, 2): 4, 6, 8

for i in range(1, 5, 1):
    print(i, end=" ")
print("")

for i in range(4, 9, 2):
    print(i, end=" ")
print("")

for i in range(5, 0, -1):
    print(i, end=" ")
print("")

for i in range(0, -6, -1):
    print(i, end=" ")
print("")