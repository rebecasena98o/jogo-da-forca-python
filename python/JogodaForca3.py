import random

# 1 - Função para mostrar o menu (Coelho)
def mostrar_menu():
    print("=== JOGO DA FORCA ===")
    print("1. Jogar")
    print("2. Sair")

# 2 - Função para carregar as palavras (Rebeca)
def carregar_palavras():
    try:
        with open("palavras.txt", "r", encoding="utf-8") as arquivo:
            palavras = [linha.strip().lower() for linha in arquivo if linha.strip()]
        return palavras
    except FileNotFoundError:
        print("Arquivo 'palavras.txt' não encontrado!")
        return []

# 3 - Função para escolher a palavra (Rebeca)
def escolher_palavra(palavras):
    return random.choice(palavras)

# 4 - Função para mostrar o progresso da palavra (Coelho)
def mostrar_palavra(palavra, letras_usuario):
    exibicao = ""
    for letra in palavra:
        if letra in letras_usuario:
            exibicao += letra + " "
        else:
            exibicao += "_ "
    print("Palavra: " + exibicao.strip() , "\n")

# 5 - Função para mostrar histórico de acertos e erros (Yan)
def mostrar_historico(letras_certas, letras_erradas):
    print("Letras certas: ", " , ".join(letras_certas) , "\n")
    
    print("Letras erradas:", " , ".join(letras_erradas) , "\n")

# 6 - Função principal do jogo (Yan)
def jogar_forca():
    palavras = carregar_palavras()

    if not palavras:
        print("Não foi possível carregar palavras para o jogo.")
        return  # Sai da função e volta para o menu

    palavra = escolher_palavra(palavras)
    letras_usuario = []
    letras_erradas = []
    letras_certas = []
    chances = 5

    while True:
        mostrar_palavra(palavra, letras_usuario)
        mostrar_historico(letras_certas, letras_erradas)

        if chances == 0:
            print("\nVocê perdeu! A palavra era:", palavra)
            break

        if all(letra in letras_usuario for letra in palavra):
            print("\nParabéns! Você acertou a palavra:", palavra)
            break

        tentativa = input("Escolha uma letra: ").lower()

        if not tentativa.isalpha() or len(tentativa) != 1:
            print("Digite apenas uma letra válida!")
            continue

        if tentativa in letras_usuario:
            print("Você já tentou essa letra!")
            continue

        letras_usuario.append(tentativa)

        if tentativa in palavra:
            letras_certas.append(tentativa)
            print("Boa! Você acertou uma letra.")
        else:
            letras_erradas.append(tentativa)
            chances -= 1
            print(f"Letra errada. Você tem {chances} chances restantes.")

# Execução principal
while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")
    print("\n")
    

    if opcao == "1":
        jogar_forca()
    elif opcao == "2":
        print("Saindo do jogo. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
