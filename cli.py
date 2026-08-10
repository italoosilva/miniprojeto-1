"""Menu interativo no terminal.

Uso: python cli.py catalogo_final.json
"""

from catalogo import Catalogo

catalogo = Catalogo("catalogo_final.json")

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
    while True: 
        exibir_menu()
        n = input()

        if n == "1":
            for i in (catalogo.listar_usuarios()):
                print(i)

            
        elif n == "2":
            nome = input("Nome de usuário: ")
            usuario_id = catalogo.buscar_usuario_por_nome(nome)
    
            if usuario_id:
                playlist_ids = catalogo.playlist_de(usuario_id)
                print(f"\nPlaylist de {nome}:")
                if playlist_ids:
                    for i in range(len(playlist_ids)):
                        titulo = catalogo.conteudos_por_id[playlist_ids[i]]["titulo"]
                        print(f"{i+1}. {titulo}")
                    print()
                else:
                    print("Playlist vazia.")
            else:
                print("Usuário não encontrado.")
                print()


        elif n == "3":
            nome = input("Nome de usuário: ")
            usuario_id = catalogo.buscar_usuario_por_nome(nome)

            if usuario_id:
                playlist = catalogo.playlist_de(usuario_id)
                if playlist:
                    num = len(playlist)
                    print(f"Playlist de {nome.title()} tem {num} itens (posições de 1 a {num}).")
                    posicao_str = input("Posição: ")

                    if posicao_str.isdigit():
                        posicao = int(posicao_str)
                        cid = catalogo.conteudo_na_posicao(usuario_id, posicao - 1)
                        if cid:
                            titulo = catalogo.conteudos_por_id[cid]["titulo"]
                            print(f"Posição {posicao} de {nome.title()}: {titulo}.")
                        else:
                            print("Posição inválida.")
                    else:
                        print("Posição inválida.")
                else:
                    print("Playlist vazia.")
            else:
                print("Usuário não encontrado.")

        elif n == "4":
            nomes = input("Nomes dos usuários separados po vírgula (ex: Nicholas, Uchoa): ").split(",")
            nomes = [nome.strip() for nome in nomes]

            if len(nomes) == 1:
                print("Informe pelo menos 2 usuários.")
            else:
                user_ids = []
                for i in nomes:
                    user = catalogo.buscar_usuario_por_nome(i)

                    if not user:
                        print(f"Usuário não encontrado.\n")
                        break

                    user_ids.append(user)

                if len(nomes) == len(user_ids):
                    intersecao = catalogo.intersecao_playlists(user_ids)

                    if not intersecao:
                        print(f"Não foram encontradas interseções.\n")
                    else:
                        print(f"Interseção ({len(intersecao)} conteúdos): ")
                        for i in intersecao:
                            print(f"- {catalogo.conteudos_por_id[i]["titulo"]}")
                        print()
                else:
                    print(f"Não foram encontradas interseções.\n")

        elif n == "5":
            conteudo_id = input("ID do conteúdo (ex: t000000): ")

            if conteudo_id in catalogo.conteudos_por_id:
                conteudo = catalogo.conteudos_por_id[conteudo_id]
                print(f"{conteudo['titulo']}")
                print(f"\trating: {catalogo.rating_de(conteudo_id)}")
                print(f"\tduração: {catalogo.duracao_total_de(conteudo_id)} seg")
                
                generos = catalogo.generos_de(conteudo_id)
                print(f"\tgêneros: {', '.join(generos) if generos else 'Nenhum'}")
                
                plataformas = catalogo.plataformas_de(conteudo_id)
                print(f"\tplataformas: {', '.join(plataformas) if plataformas else 'Nenhuma'}")
                
                print(f"\tadicionado: {catalogo.data_adicionado_de(conteudo_id)}")
                
                execucoes = catalogo.execucoes_de(conteudo_id)
                if execucoes is not None:
                    print(f"Execuções: {execucoes}")
            else:
                print(f"Conteúdo não encontrado.\n")


        elif n == "6":
            genero = input("Gênero (ex: Pop): ")

            generos = catalogo.conteudos_do_genero(genero)
            if generos:
                for i in generos:
                    titulo = catalogo.conteudos_por_id[i]["titulo"]
                    print(f"- {titulo}")
            else:
                print(f"Nenhum conteúdo encontrado para o gênero '{genero}'.\n")


        elif n == "7":
            conteudo_id = input("ID do conteúdo a enfileirar (ex: t000000): ")

            if catalogo.enfileirar(conteudo_id):
                num = len(catalogo.fila_atual())
                titulo = catalogo.conteudos_por_id[conteudo_id]["titulo"]
                print(f"Enfileirado: '{titulo}' (fila com {num} item).")
            else:
                print(f"Conteúdo '{conteudo_id}' não encontrado.\n")
            


        elif n == "8":
            proximo_id = catalogo.proximo()

            if proximo_id:
                num = len(catalogo.fila_atual())
                titulo = catalogo.conteudos_por_id[proximo_id]["titulo"]
                print(f"Tocando: '{titulo}'.")
                print(f"Restam: {num} itens na fila\n")
            else:
                print(f"Tocando: undefined.")
                print(f"Restam: {num} itens na fila")



        elif n == "9":
            fila = catalogo.fila_atual()

            if fila:
                print(f"Fila atual ({len(fila)} itens):")
                for i in range(len(fila)):
                    cid = fila[i]
                    titulo = catalogo.conteudos_por_id[cid]["titulo"]
                    print(f"{i+1}. {titulo}")
                print()
            else:
                print(f"Fila vazia.\n")


        elif n == "10":
            break


        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()