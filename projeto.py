import os 
import sys 

ARQUIVO = "plateia.txt"

def menu():
    print("-------------------------")
    print("0 - Sair")
    print("1 - Mostrar plateia ")
    print("2 - Mostrar ocupação")
    print("3 - Vender Ingresso")
    print("4 - Cancelar Ingresso (devolução)")
    escolhe_opcao()

def validaOpcao (opcao, min, max):
    while True: 
        try:
            opcao = int(opcao)
            if opcao < min or opcao > max:
                print(f"Valor inválido. Digite um número entre {min} e {max}")
                opcao = input("Digite novamente: ")
            else:
                return opcao
        except ValueError:
            print("Entrada inválida. Digite um número!")
            opcao = input("Digite novamente: ")

def escolhe_opcao():

    while True:
        opcao = input("Digite a opção: ")
        opcao = validaOpcao(opcao,0,4)    

        if opcao == 1:
            mostra_plateia()
            menu()
        elif opcao == 2:
            mostra_ocupacao()
            menu()
        elif opcao == 3:
            vender_ingresso()
            menu()
        elif opcao == 4:
            print()
            menu()
        elif opcao == 0:
            os.system('cls')
            print("Saindo do programa....")
            sys.exit()
            break

#CRIAÇÃO, LEITURA E SALVAMENTO DE MATRIZ E ARQUIVO 
def carregar_dados (nome_arquivo):
    if os.path.exists(nome_arquivo):
        arq = open(nome_arquivo, 'r')
        dados = []
        for linha in arq:
            dados.append(list(linha.strip()))
        arq.close()
        return dados
    else:
        dados = [['-' for j in range (12)] for i in range (10)]
        salvar_dados(nome_arquivo,dados)
        return dados
    

def salvar_dados(nome_arquivo, dados):
    arq = open(nome_arquivo, 'w')
    for linha in dados:
        arq.write("".join(linha) + '\n')
    arq.close()
    print("Matriz salva em: ", nome_arquivo)

def exibir_matriz(matriz):
    contador = 1
    print("-------------------------")
    print("\n Plateia:")
    print("-------------------------")
    for linha in matriz:
        for assento in linha:
            if assento == '-':
                print(f"{contador:3}", end=" ")
            else:
                print("   ", end= "")
            contador += 1
        print()
    print("\nFim da Plateia")

def mostra_plateia():
    plateia = carregar_dados(ARQUIVO)
    exibir_matriz(plateia)

def mostra_ocupacao():
    meia = 0; inteira = 0
    plateia = carregar_dados(ARQUIVO)
    
    print("Ocupação:")
    print("-------------------------")

    for linha in plateia:
        for assento in linha:
            if assento.lower() == 'm': 
                meia += 1
            if assento.lower() == 'i':
                inteira  +=1
            print(f"{assento}", end=" ")
        print()
    print("-------------------------")       
    print(f"Foram vendidas {meia} poltronas meia")
    print(f"Foram vendidas {inteira} poltronas inteira")
    print("-------------------------\nFim da ocupação")

def vender_ingresso():
    plateia = carregar_dados(ARQUIVO)
    while True:
        mostra_plateia()
        while True:
            poltrona = validaOpcao(input("Digite a poltrona desejada <1.120> (0 encerra): "),0 , 120)
            if poltrona == 0:
                print("Fim da venda de ingressos")
                return
            linha = (poltrona - 1) // 12
            coluna = (poltrona - 1) % 12
            
            if plateia[linha][coluna] != '-':
                print("Poltrona ocupada. Tente novamente.")
            else:
                break
        while True:
            entrada = input("Digite o tipo da entrada (m)eia ou (i)nteira: ").strip().upper()
            if entrada != 'M' or 'I':
                break
            else:
                print("Entrada inválida. Digite M ou I!")
        
        plateia[linha][coluna] = entrada
        salvar_dados(ARQUIVO, plateia)

        continuar = validaOpcao(input("Deseja vender outro ingresso? (1)Sim (0)Não: "),0,1)
        if continuar == 0:
            print("Venda de ingressos encerrada.")
            break


def cancel_ingresso():
    print()

# -------------------------------------------------------------
# main()
menu()