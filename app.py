
# Agenda 11 - Desenvolvimento de Sistemas I
# Projeto: Controle de Níveis de Água

from colorama import Fore, Style, init

# Inicializa a biblioteca Colorama
init(autoreset=False)

# Lista com as situações do reservatório
situacoes = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]


# Função responsável por definir a cor
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE


# Função para exibir a situação do reservatório
def exibir_situacao(nivel):
    if 1 <= nivel <= len(situacoes):
        mensagem = situacoes[nivel - 1]
        cor = definir_cor(nivel)

        print(cor + f"Nível {nivel}: {mensagem}"
              + Style.RESET_ALL)
    else:
        print("Erro: nível inválido!")


# Programa principal
print("=== CONTROLE DE NÍVEIS DE ÁGUA ===")

# Simulação dos cinco níveis
print("\nSimulação dos níveis do reservatório:\n")

for nivel in range(1, 6):
    exibir_situacao(nivel)

# Define o nível atual do reservatório
nivel_atual = 3

print("\n=== SITUAÇÃO ATUAL ===")
exibir_situacao(nivel_atual)

# Restaura o estilo padrão do terminal
print(Style.RESET_ALL)
