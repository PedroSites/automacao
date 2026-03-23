

# Lista de nomes
nomes = ["Giovana","Mateus","Goão","Pietro","Thiago","Kessy"]

for n, nome in enumerate(nomes):
    print(f"Estou no indice {n} que possui nome {nome}")
    if nome == "Goão":
        nomes[n] = "João"
        break

print(nomes)