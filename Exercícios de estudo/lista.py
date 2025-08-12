# exercício.append #1:

nomes = []

for i in range(3):
    nome=(input(f"Digite o {i + 1}º nome: "))
    nomes.append(nome)

print(nomes)

# exercício.append #2:

numeros = []

for i in range(5):
    numero=(int(input(f"Digite o {i + 1}º número: ")))
    numeros.append(numero)

print("O maior número digitado foi:", max(numeros))

# exercício.append #3:

compras = []
resposta = "CONTINUAR"

while resposta == "CONTINUAR":
    compras.append(input("Digite um item para sua compra: "))
    resposta=input("Digite \"continuar\" para incrementar mais itens em sua lista: ").upper()


print("Sua lista de compras: ", compras)


# exercício.append #4:

idades = []

for i in range(4):
    idade=int(input(f"Digite a {i + 1}° idade: "))
    idades.append(idade)

media= sum(idades) / 4 
print(f"A média das idades é : {media}")

# exercício.append #5:

