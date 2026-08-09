"""Menu interativo no terminal.

Uso: python cli.py catalogo_final.json
"""
def exibir_menu():
    print("Trilha Sonora")
    print("----------------")
    print("1. Listar todos os usuários")
    print("2. Ver playlist completa de um usuário")
    print("3. Conteúdo na posição N da playlist")
    print("4. Interseção de playlists (N usuários)")
    print("5. Dados de um conteúdo (rating, duração, gêneros, plataformas, data, execuções)")
    print("6. Conteúdos de um gênero")
    print("7. Enfileirar conteúdo na fila de reprodução")
    print("8. Tocar próximo da fila")
    print("9. Ver fila atual")
    print("10. sair")


def main(): 
    exibir_menu()
    n = input()

    if n == "1":
        print("teste")

        
    elif n == "2":
        pass


    elif n == "3":
        pass


    elif n == "4":
        pass


    elif n == "5":
        pass


    elif n == "6":
        pass


    elif n == "7":
        pass


    elif n == "8":
        pass


    elif n == "9":
        pass


    elif n == "10":
        return


    else:
        print("Opção inválida.")









if __name__ == "__main__":
    main()