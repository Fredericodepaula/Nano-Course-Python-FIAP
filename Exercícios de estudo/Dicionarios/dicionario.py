from funcoes import *

usuarios = {}

opcao = perguntar()

while opcao =="I" or opcao =="P" or opcao =="E" or opcao =="L":
    if opcao == "I":
        inserir_usuario(usuarios)
        opcao = perguntar()
