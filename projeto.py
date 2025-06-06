
def menu():
    print("-------------------------")
    print("0 - Sair")
    print("1- Mostrar plateia ")
    print("2 - Mostrar ocupação")
    print("3 - Vender Ingresso")
    print("4 - Cancelar Ingresso (devolução)")
    escolhe_opcao()


def escolhe_opcao():
    opcao = int(input("Digite a opção: "))
    while True:
        if opcao == 1:
            mostra_plateia()
            menu()
        elif opcao == 2:
            print("Deu boa")
            menu()
        elif opcao == 3:
            print()
            menu
        elif opcao == 4:
            print()
            break
        elif opcao == 0:
            break
    


def mostra_plateia():
    print("Deu boa")
    return 0
def mostra_ocupacao():
    print()
def vender_ingresso():
    print()
def cancel_ingresso():
    print()

menu()