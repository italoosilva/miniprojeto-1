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





def listar_usuarios():
    pass


def buscar_usuario_por_nome():
    pass


def rating_de():
    pass


def duracao_total_de():
    pass



if __name__ == "__main__":
    cat = Catalogo("catalogo_dev.json")
    print("Quantidade de itens carregados:", len(cat.conteudos_por_id))
    print("Exemplo de item guardado:", cat.conteudos_por_id.get("t000002"))