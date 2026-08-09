import json


def valores_iguais(val_gabarito, val_resposta):
    if type(val_gabarito) != type(val_resposta):
        return False

    if isinstance(val_gabarito, float):
        return abs(val_gabarito - val_resposta) < 1e-6

    if isinstance(val_gabarito, list):
        if len(val_gabarito) != len(val_resposta):
            return False
        return all(valores_iguais(g, r) for g, r in zip(val_gabarito, val_resposta))

    if isinstance(val_gabarito, dict):
        if set(val_gabarito.keys()) != set(val_resposta.keys()):
            return False
        return all(valores_iguais(val_gabarito[k], val_resposta[k]) for k in val_gabarito)

    return val_gabarito == val_resposta


def conferir():
    try:
        with open("gabarito_publico.json", "r", encoding="utf-8") as f:
            gabarito = json.load(f)
    except FileNotFoundError:
        print("Erro: Arquivo 'gabarito_publico.json' nao foi encontrado.")
        return

    try:
        with open("respostas.json", "r", encoding="utf-8") as f:
            respostas = json.load(f)
    except FileNotFoundError:
        print("Erro: Arquivo 'respostas.json' nao foi encontrado.")
        return

    total = len(gabarito)
    acertos = 0
    erros = 0
    ausentes = 0

    print("--- CONFERENCIA DE RESPOSTAS ---\n")

    for chave, val_esperado in gabarito.items():
        if chave not in respostas:
            print(f"[ERRO] Chave {chave} AUSENTE no seu respostas.json")
            ausentes += 1
            continue

        val_gerado = respostas[chave]

        if valores_iguais(val_esperado, val_gerado):
            print(f"[OK] Chave {chave}")
            acertos += 1
        else:
            print(f"[ERRO] Chave {chave} INCORRETA")
            print(f"   Esperado: {val_esperado}")
            print(f"   Obtido:   {val_gerado}")
            erros += 1

    print("\n--- RESUMO FINAL ---")
    print(f"Total de testes: {total}")
    print(f"Acertos: {acertos}/{total}")
    print(f"Erros: {erros}")
    print(f"Chaves ausentes: {ausentes}")


if __name__ == "__main__":
    conferir()