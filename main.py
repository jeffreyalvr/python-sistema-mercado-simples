import math
import sys

# variável para determinar em qual menu o usuário estará
comando = 0

# listas para exibir os produtos disponíveis e quais produtos estão no carrinho do cliente
catalogo_produtos = ['maçã', 'banana', 'uva', 'mamão', 'pêssego']
carrinho_produtos = []

# mensagem inicial de boas vindas
print('Bem-vindo ao Sistema de Mercadinho!\n')

# função para exibir o menu inicial
def mostrar_menu():
    print('\n1. Inciar uma nova compra')
    print('2. Adicionar produto ao catálogo')
    print('3. Remover produto do catálogo')
    print('4. Sair do programa')

    # pega o input do usuário com o valor desejado
    comando = int(input('\nSelecione uma opção digitando um número: '))

    # envia o valor para a função valida_input
    valida_input(comando)

# função para exibir o menu de compra
def compra():
    indice = 0 # inicia uma variável indice com valor 0, para se ajustar a lista
    deseja_continuar = 's'

    print('\nCatálogo de Produtos: ')

    while (deseja_continuar == 's'):
        for i in catalogo_produtos:
            print('{0} - {1}'.format(indice, i)) # exibe o indice no loop atual e o item da lista
            indice += 1 # adiciona +1 em indice
            item = input('\nDigite um número para o item desejado: ')
            carrinho_produtos.append(item)

            deseja_continuar = str(input("Digite 'S' se deseja selecionar outro item OU digite 'N' se deseja finalizar o carrinho: "))

            # transforma o valor dentro de deseja_continuar para minúsculo, a fim de evitar erros de comparação
            deseja_continuar.lower()

            # verifica se deseja_continuar possui um valor diferente de 's' ou 'n', caso True, seta um valor default
            if (deseja_continuar != 's' and deseja_continuar != 'n'):
                print('Comando inválido! Retornando...')
                deseja_continuar = 's'

            # se a resposta é 'n' então saia do loop
            if (deseja_continuar == 'n'):
                break
    mostrar_carrinho() # chama mostrar_carrinho caso saia do while

# função para adicionar um produto ao catálogo de produtos
def adicionar_produto():
    print('adiciona produto')

# função para remover um produto do catálogo de produtos
def remover_produto():
    print('remove produto')

# função para exibir o carrinho de compras do cliente atual
def mostrar_carrinho():
    print('Você adicionou os seguintes itens ao carrinho:')
    for i in carrinho_produtos:
        print(i)

    print("\nPara finalizar o carrinho digite '0'")
    print("Para adicionar mais itens ao carrinho digite '1'")
    print("Para remover itens do carrinho digite '2'")
    opcao = int(input('\nOpção desejada: '))

    if (opcao == 0):
        finalizar_carrinho()
    elif (opcao == 1):
        compra()
    elif (opcao == 2):
        remover_produto_carrinho()
    else:
        print('Comando inválido! Retornando...')
        mostrar_carrinho()

# função para remover um produto do carrinho de compras do cliente atual
def remover_produto_carrinho():
    deseja_continuar = 's'

    while (deseja_continuar == 's'):
        print('\nVocê adicionou os seguintes itens: {0}'.format(carrinho_produtos))
        item = int(input('\nDigite o número correspondente ao item que deseja remover: '))
        carrinho_produtos.remove(str(item))

        deseja_continuar = str(input("Deseja remover mais algum item? Digite 'S' para confirmar e 'N' para fechar o carrinho: "))

        # transforma o valor dentro de deseja_continuar para minúsculo, a fim de evitar erros de comparação
        deseja_continuar.lower()

        # verifica se deseja_continuar possui um valor diferente de 's' ou 'n', caso True, seta um valor default
        if (deseja_continuar != 's' and deseja_continuar != 'n'):
            print('\nComando inválido! Retornando...')
            deseja_continuar = 's'

        # se a resposta é 'n' então saia do loop
        if (deseja_continuar == 'n'):
            break
    finalizar_carrinho() # chama finalizar_carrinho caso saia do while

# função para finalizar a compra e reexibir o menu
def finalizar_carrinho():
    print('\nCompra finalizada. Obrigado!')
    mostrar_menu()

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
    if (valor == 0):
        mostrar_menu()
    elif (valor == 1):
        compra()
    elif (valor == 2):
        adicionar_produto()
    elif (valor == 3):
        remover_produto()
    elif (valor == 4):
        sair()

# exibe inicialmente o menu
mostrar_menu()