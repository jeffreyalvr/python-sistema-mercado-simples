import math
import sys

# variável para determinar em qual menu o usuário estará
comando = 0

# mensagem inicial de boas vindas
print('Bem-vindo ao Sistema de Mercadinho!\n')

# função para exibir o menu inicial
def mostrar_menu():
    print('1. Inciar uma nova compra')
    print('2. Adicionar produto ao catálogo')
    print('3. Remover produto do catálogo')
    print('4. Sair do programa')

    # pega o input do usuário com o valor desejado
    comando = int(input('\nSelecione uma opção digitando um número: '))

    # envia o valor para a função valida_input
    valida_input(comando)

# função para terminar a aplicação
def sair():
    print('\nDeseja sair da aplicação?')
    comando = int(input("Digite '0' para sair ou '1' para cancelar e voltar ao menu: "))
    if (comando == 0):
        sys.exit() # termina a aplicação
    else:
        mostrar_menu()

# função que verifica qual o input dado pelo usuário e exibe o menu correspondente
def valida_input(valor):
    import compra
    import catalogo

    if (valor == 0):
        mostrar_menu()
    elif (valor == 1):
        compra.compra()
    elif (valor == 2):
        catalogo.adicionar_produto()
    elif (valor == 3):
        catalogo.remover_produto()
    elif (valor == 4):
        sair()

# exibe inicialmente o menu
mostrar_menu()