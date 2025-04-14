from datetime import datetime

def registrar_hora(caminho_arquivo):
    hora_atual = datetime.now().strftime("%H:%M:%S")
    with open(caminho_arquivo, "a") as arquivo:
        arquivo.write(f"Executado em: {hora_atual}\n")
    return hora_atual
