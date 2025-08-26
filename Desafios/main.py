from funcoes import *

print("=== Sistema de Cadastro De Alunos === ")

alunos = cadastrar_aluno()


medias = calcular_media(alunos)

print("\n=== Médias dos Alunos ===")
for nome, media in medias.items():
    print(f"{nome}: {media:.2f}")