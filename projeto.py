import os 

ARQUIVO = "plateia.txt"

def menu():
    print("-------------------------")
    print("0 - Sair")
    print("1- Mostrar plateia ")
    print("2 - Mostrar ocupação")
    print("3 - Vender Ingresso")
    print("4 - Cancelar Ingresso (devolução)")
    escolhe_opcao()

def validaOpcao (opcao, min, max):
    if opcao.isdigit():
        opcao = int(opcao)
        if opcao < min or opcao > max:
            print(f"Entrada inválida, digite um número entre {min} e {max}")
            return escolhe_opcao()
        else:
            return opcao
    else:
        print("Valor inválido, digite um número!")
        return escolhe_opcao()

def escolhe_opcao():

    while True:
        opcao = input("Digite a opção: ")
        opcao = validaOpcao(opcao,0,4)    

        if opcao == 1:
            mostra_plateia()
            menu()
        elif opcao == 2:
            print("Deu boa")
            menu()
        elif opcao == 3:
            print()
            menu()
        elif opcao == 4:
            print()
            break
        elif opcao == 0:
            os.system('cls')
            print("Saindo do programa....")
            break

def carregar_dados (nome_arquivo):
    if os.path.exists(nome_arquivo):
        arq = open(nome_arquivo, 'r')
        dados = []
        for linha in arq:
            dados.append(list(linha.strip()))
        arq.close()
        return dados
    else:
        return [['-' for j in range (12)] for i in range (10)]
    
    
def salvar_dados(nome_arquivo, dados):
    arq = open(nome_arquivo, 'w')
    for linha in dados:
        arq.write("".join(linha) + '\n')
    arq.close()
    print("Matriz salva em: ", nome_arquivo)

def exibir_matriz(matriz):
    print("\n Matriz atual:")
    for linha in matriz:
        print(" ".join(linha))
    print()

def mostra_plateia():
    matriz = carregar_dados(ARQUIVO)
    exibir_matriz(matriz)
    salvar_dados(ARQUIVO, matriz)

def mostra_ocupacao():
    print()
def vender_ingresso():
    print()
def cancel_ingresso():
    print()

menu()