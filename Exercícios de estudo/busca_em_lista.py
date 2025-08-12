# Exercícios sobre busca em lista pelo seu nome ou número

# Exercício 1:

frutas = ["banana","maça","uva","limão","laranja"]

busca=input("Digite o nome de uma fruta: ") .lower()

if busca in frutas:
    print("Fruta encontrada!!!")

else:
    print("Fruta não encontrada")

# Exercício 2:

nomes = ["Frederico", "Priscila", "Guilherme", "Valentina" , "Liz", "Giovana"]

busca = input("Digite o nome para buscar na lista: ") 

if busca in nomes:
    print(f"Nome encontrado no indice {nomes.index(busca)}")
else:
    print("Esse nome não esta na lista ")
