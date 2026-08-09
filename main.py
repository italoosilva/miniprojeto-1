"""Modo batch: lê consultas.json, responde em ordem, grava respostas.json.

Uso: python main.py consultas.json respostas.json
"""
import json
import sys
from catalogo import Catalogo


def executar_batch(caminho_consultas: str, caminho_respostas: str):
    catalogo = Catalogo("catalogo_final.json")

    with open(caminho_consultas, "r", encoding="utf-8") as f:
        dados_consultas = json.load(f)

    respostas = {}
    consultas = dados_consultas.get("consultas", [])

    for consulta in consultas:
        cid_str = str(consulta["id"])
        nome_metodo = consulta["tipo"]
        parametros = consulta.get("parametros", {})

        metodo = getattr(catalogo, nome_metodo)
        resultado = metodo(**parametros)

        respostas[cid_str] = resultado

    with open(caminho_respostas, "w", encoding="utf-8") as f:
        json.dump(respostas, f, indent=2, ensure_ascii=False)

    print(f"Respostas geradas com sucesso! Total de consultas processadas: {len(consultas)}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(1)

    arquivo_entrada = sys.argv[1]
    arquivo_saida = sys.argv[2]

    executar_batch(arquivo_entrada, arquivo_saida)