# lista para exibir quais produtos estão no carrinho do cliente
carrinho_produtos = []

# função para exibir o carrinho de compras do cliente atual
def mostrar_carrinho():
    import compra

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
        compra.compra()
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
    print('\nCompra finalizada. Obrigado!\nRetornando ao menu...\n')

    import main
    main.mostrar_menu()