# Exercício 1:

produtos = []
resposta = "S"

while resposta == "S":
    nome=input("Digite o nome do produto: ")
    preco=float(input("Digite o preço do produto: "))
    quantidade=int(input("Digite a quantidade de produto disponível: "))
    produtos.append([nome, preco, quantidade])
    resposta=input("Digite \"S\" para continuar adicionando produtos: ").upper()

print("Lista de Produtos: ")

for produto in produtos:
    print(f"Produto:{produto[0]}, Preço:{produto[1]}, Quantidade:{produto[2]}")

# Exercício 2:

alunos = []
resposta = "S"

while resposta == "S":
    nome = input("Digite o Nome do Aluno: ")
    nota1 = float(input("Digite a 1° Nota do Aluno: "))
    nota2 = float(input("Digite a 2° Nota do Aluno: "))
    alunos.append([nome,nota1,nota2])
    resposta=input("Digite \"S\" para continuar adicionando alunos: ").upper()

print("Alunos com sua Média: ")

for aluno in alunos:
    media = (aluno[1] + aluno[2]) / 2
    print(f"Aluno:{aluno[0]}, Média:{media}")

# Exercício 3:

lista_contatos = []
resposta = "S"

while resposta == "S":
    nome=input("Digite o Nome: ")
    telefone=input("Digite o Telefone: ")
    email=input("Digite o e-mail: ")
    lista_contatos.append([nome,telefone,email])
    resposta=input("Digite \"S\" Para Continuar Inserindo Contatos Na Sua Lista: ").upper()

pesquisa=input("Digite O nome do Contato Que Quer Buscar: ")

for contato in lista_contatos:
    if contato[0] == pesquisa:
        print(f"Nome:{contato[0]}, Telefone:{contato[1]}, Email:{contato[2]}")
        break
else:
    print("Contato Não Encontrado")