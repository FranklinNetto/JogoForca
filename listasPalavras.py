import random

def define_palavra_chave():

    arquivo = open("palavrasForca.txt", "r", encoding="utf-8")

    palavras = []

    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)

    arquivo.close()

    indice = random.randrange(0, len(palavras))

    return palavras[indice]
