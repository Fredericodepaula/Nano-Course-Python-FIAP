def cadastrar_aluno():
    alunos = {}
    resposta = "S"
    while resposta == "S":
        nome = input("Digite o Nome do Aluno: ")
        notas = [
            float(input("Digite a 1ª nota: ")),
            float(input("Digite a 2ª nota: ")),
            float(input("Digite a 3ª nota: "))
        ]
        alunos[nome] = notas
        resposta = input("Digite \"S\" para Continuar Inserindo alunos: ").upper()
    return alunos 

def calcular_media(alunos):
    medias = {}
    for nome, notas in alunos.items():
        media = sum(notas) / len(notas)
        medias[nome] = media
    return medias
   