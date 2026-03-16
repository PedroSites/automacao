# Entrada
titulo = str(input("Digite o nome do filme: "))
diarias = int(input("Digite a diaria alugada: "))
tempo = int(input("Digite quantos dias a pessoa ficou: "))

# Processamento
valor = tempo * 5
multa = 0

if tempo - diarias > 0:
    multa = 15

total = valor + multa

# Saida
print(f"O valor a ser pago é R${total:.2f}")