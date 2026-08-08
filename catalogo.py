"""A classe Catalogo. Leia o README.md antes de começar.

Esta é a peça central do projeto: carrega o JSON uma vez, constrói os
índices no __init__ e expõe os 16 métodos que o main.py e o cli.py usam.
"""

import json

def limpar_rating(rating):
    if rating is None:
        return None
    return float(rating)

def limpar_data(data_str):
    if not data_str:
        return None
    
    if "/" in data_str:
        dia, mes, ano = data_str.split("/")
        return f"{ano}-{mes}-{dia}"

    return data_str

def limpar_execucoes(execucoes):
    if not execucoes:
        return None

    if isinstance(execucoes, str):
        limpo = execucoes.replace(",", "")
        return int(limpo)

    return int(execucoes)
    
def limpar_generos(generos):
    if isinstance(generos,str):
        return [generos]

    resultado = []
    pilha = list(generos)

    while pilha:
        item = pilha.pop()

        if isinstance(item, str):
            resultado.append(item)
        elif isinstance(item, list):
            for i in item:
                resultado.append(i)

    return sorted(resultado)





class Catalogo:
    def __init__(self, caminho_json: str):
        with open(caminho_json, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        self.fila = []

        self.conteudos_por_id = {}
        for item in dados.get("conteudos", []):
            item["rating"] = limpar_rating(item.get("rating"))
            item["data_adicionado"] = limpar_data(item.get("data_adicionado"))
            item["generos"] = limpar_generos(item.get("generos"))

            if "engajamento" in item and "execucoes" in item["engajamento"]:
                item["engajamento"]["execucoes"] = limpar_execucoes(item["engajamento"]["execucoes"])

            item_id = item["id"]
            self.conteudos_por_id[item_id] = item
            
        self.usuarios_por_nome = {}
        for usuario in dados.get("usuarios", []):
            nome_minusculo = usuario["nome"].lower()
            self.usuarios_por_nome[nome_minusculo] = usuario


    def listar_usuarios(self) -> list[str]:
        return sorted([user["nome"] for user in self.usuarios_por_nome.values()])


    def buscar_usuario_por_nome(self,nome):
        nome_limpo = nome.lower()
        if nome_limpo in self.usuarios_por_nome:
            return self.usuarios_por_nome[nome_limpo]["id"]
        return None



    def playlist_de(self, usuario_id: str) -> list[str] | None:
        for user in self.usuarios_por_nome.values():
            if usuario_id == user["id"]:
                return user["playlist"]
        return None


    def conteudo_na_posicao(self, usuario_id: str, posicao: int) -> str | None:
        playlist = self.playlist_de(usuario_id)

        if playlist is not None and 0 <= posicao < len(playlist):
            return playlist[posicao]
        return None


    def intersecao_playlists(self, usuario_ids: list[str]) -> list[str]:
        if not usuario_ids:
            return []
        
        for id in usuario_ids:
            if self.playlist_de(id) == None:
                return[]

        intersecao = []
        playlist1 = self.playlist_de(usuario_ids[0])

        for music in playlist1:
            em_todos = True
            for uid in usuario_ids[1:]:
                teste = self.playlist_de(uid)
                if teste is None or music not in teste:
                    em_todos = False
                    break

            if em_todos:
                intersecao.append(music)

        return intersecao




    def rating_de(self, conteudo_id: str) -> float | None:
        if conteudo_id in self.conteudos_por_id:
            return self.conteudos_por_id[conteudo_id]["rating"]
        return None


    def duracao_total_de(self, conteudo_id: str) -> int | None:
        if conteudo_id in self.conteudos_por_id:
            duracao = 0

            if self.conteudos_por_id[conteudo_id]["tipo"] == "album":
                for faixa in self.conteudos_por_id[conteudo_id]["faixas"]:
                    if faixa["duracao_seg"] is not None:
                        duracao += faixa["duracao_seg"]
                return duracao
            else:
                return self.conteudos_por_id[conteudo_id]["duracao_seg"]
        return None


    def generos_de(self, conteudo_id: str) -> list[str] | None:
        if conteudo_id in self.conteudos_por_id:
            return self.conteudos_por_id[conteudo_id]["generos"]
        return None


    def plataformas_de(self, conteudo_id: str) -> list[str] | None:
        if conteudo_id in self.conteudos_por_id:
            return self.conteudos_por_id[conteudo_id]["plataformas"]
        return None

    
    def data_adicionado_de(self, conteudo_id: str) -> str | None:
        if conteudo_id in self.conteudos_por_id:
            return self.conteudos_por_id[conteudo_id]["data_adicionado"]
        return None


    def execucoes_de(self, conteudo_id: str) -> int | None:
        if conteudo_id in self.conteudos_por_id and self.conteudos_por_id[conteudo_id]["tipo"] == "musica":
            return self.conteudos_por_id[conteudo_id]["engajamento"]["execucoes"]
        return None

        
    def conteudos_do_genero(self, genero: str) -> list[str]:
        resultado = []
        for cid, item in self.conteudos_por_id.items():
            generos = item.get("generos")
            if generos and genero in generos:
                resultado.append(cid)
        return resultado


    def enfileirar(self, conteudo_id: str) -> bool:
        if conteudo_id in self.conteudos_por_id:
            self.fila.append(conteudo_id)
            return True
        return False


    def proximo(self) -> str | None:
        if not self.fila:
            return None
        return self.fila.pop[0]

    def fila_atual(self) -> list[str]:
        return list(self.fila_atual)


if __name__ == "__main__":
    cat = Catalogo("catalogo_dev.json")
    print("Quantidade de itens carregados:", len(cat.conteudos_por_id))
    print("Exemplo de item guardado:", cat.conteudos_por_id.get("t000002"))