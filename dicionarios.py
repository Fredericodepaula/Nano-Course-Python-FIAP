# usuarios = {}
# print(usuarios)

# usuarios = {
#     "chaves" : ["Chaves do 8", "21/08/2025", "Recep_01"],
#     "quico" : ["Quico das Flores", "21/08/2025", "Recep_02"]
# }

# print(usuarios)

# usuarios["florinda"] = ["Dona Florinda", "20/08/2025", "Raiox_03"]

# print(usuarios)

# print(usuarios.get("chaves"))

# Controle de usuários:

usuarios = {}

opcao= input("<I> para inserir o usuário\n"+
             "<P> para pesquisar usuário\n"+
             "<E> para excluir usuário\n"+  
             "<L> para listar um usuário\n").upper()

while opcao =="I" or opcao =="P" or opcao =="E" or opcao =="L":
    if opcao == "I":
        chave=input("Digite o login o usuário: ").upper()
        nome=input("Digite o nome do usuário: ").upper()
        data=input("Digite a ultima data de acesso: ")
        usuarios[chave] = [nome , data]

print(usuarios)