# Estrutura de repetição For para listas
# Lista: estrutura de dados composta (armazena varios valores)

# cria uma lista de nomes
nomes = ["Pietro", "Ryan","Mariana","Grabriela","Sophia"]

# imprime toda a lista
print(f"{nomes}")

# imprime um nome expecifico (Mariana)
print(f"{nomes[2]}")

# imprimir usando for
for i in nomes:
    print(i, end=" ")
print("")

for n, i in enumerate(nomes):
    print(f"{n}-{i}", end=" ")