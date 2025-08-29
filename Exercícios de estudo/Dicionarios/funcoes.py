def perguntar():
    return input("<I> para inserir o usuário\n"+
             "<P> para pesquisar usuário\n"+
             "<E> para excluir usuário\n"+  
             "<L> para listar um usuário\n").upper()

def inserir_usuario(dicionario):
    dicionario[input("Digite o login o usuário: ").upper()] = [input("Digite o nome do usuário: ").upper() , 
                                                                 input("Digite a ultima data de acesso: ")]
    salvar(dicionario)

def salvar(dicionario):
    with open("banco_de_dados.txt" "a") as arquivo:
     for chave,valor in dicionario.items():
        arquivo.write(chave + ":" + str(valor))
