# função para exibir o menu de compra
def compra():
    import carrinho
    import catalogo

    indice = 0 # inicia uma variável indice com valor 0, para se ajustar a lista
    deseja_continuar = 's'

    print('\nCatálogo de Produtos: ')

    while (deseja_continuar == 's'):
        for i in catalogo.catalogo_produtos:
            print('{0} - {1}'.format(indice, i)) # exibe o indice no loop atual e o item da lista
            indice += 1 # adiciona +1 em indice
            item = input('\nDigite um número para o item desejado: ')
            carrinho.carrinho_produtos.append(item)

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
    # chama mostrar_carrinho caso saia do while
    carrinho.mostrar_carrinho()