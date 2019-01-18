# função para exibir o menu de compra
def compra():
    import carrinho
    import catalogo

    # inicia uma variável indice com valor 0, para se ajustar a lista
    indice = 0
    deseja_continuar = 's'

    print('\nCatálogo de Produtos: ')

    for i in range(len(catalogo.catalogo_produtos)):
        # exibe o indice no loop atual e o item da lista
        print('{0} - {1}'.format(indice, catalogo.catalogo_produtos[i]))
        # adiciona +1 em indice
        indice += 1

    while (deseja_continuar == 's'):
        numero = int(input('\nDigite um número para o item desejado: '))
        # adiciona o item ao carrinho_produtos
        if (numero > len(catalogo.catalogo_produtos) or numero < len(catalogo.catalogo_produtos)):
            print('Número inválido! Retornando...\n')
            voltar_ao_menu()
        else:
            item = catalogo.catalogo_produtos[numero]
            carrinho.carrinho_produtos.append(item)

        deseja_continuar = str(
            input("Digite 'S' se deseja selecionar outro item OU digite 'N' se deseja finalizar o carrinho: "))

        # transforma o valor dentro de deseja_continuar para minúsculo, a fim de evitar erros de comparação
        deseja_continuar.lower()

        # verifica se deseja_continuar possui um valor diferente de 's' ou 'n', caso True, seta um valor default
        if (deseja_continuar != 's' and deseja_continuar != 'n'):
            print('Comando inválido! Retornando...\n')
            deseja_continuar = 's'

        # se a resposta é 'n' então saia do loop
        if (deseja_continuar == 'n'):
            break
    # chama mostrar_carrinho caso saia do while
    carrinho.mostrar_carrinho()

def voltar_ao_menu():
    import main
    main.mostrar_menu()