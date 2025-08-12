# Exercício 1:

nomes = []
idades = []

for i in range(3):
    nome = input(f"Digite o {i + 1}° nome: ")
    idade = int(input(f"Digite a {i + 1}° idade: "))
    nomes.append(nome)
    idades.append(idade)

print("Lista de Nomes e Idades: ")

for i in range(3):
    print(f"{nomes[i]} tem {idades[i]} anos")

# Exercício 2:

produtos = []
precos = []

for i in range(5):
    produto=input(f"Digite o {i + 1} produto: ")
    preco=float(input(f"Digite o valor do {i + 1} produto: "))
    produtos.append(produto)
    precos.append(preco)

print("Lista de seus produtos com preço:")

for i in range(5):
    print(f"O {produtos[i]} custa R${precos[i]}")