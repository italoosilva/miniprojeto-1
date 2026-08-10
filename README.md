# Mini-Projeto TrilhaSonora

Este projeto implementa o gerenciamento de um acervo musical com suporte a processamento de consultas em lote e uma interface interativa no terminal.

## Decisões de modelagem

Foi utilizada a classe `Catalogo`. Essa classe agrupa estado e comportamento que pertencem juntos porque centraliza os dados do acervo, a manipulação da fila de reprodução e as regras de consulta de usuários e playlists em uma única estrutura.

Os registros de mídias e usuários são mantidos como dicionários, pois não possuem comportamentos próprios isolados do catálogo. No método `__init__`, os dados do JSON são carregados e indexados por ID (`conteudos_por_id`) e por nome (`usuarios_por_nome`) para garantir acesso direto em tempo constante.

## Tratamento dos dados

A sanitização e padronização dos dados ocorrem no momento da carga do catálogo através de funções auxiliares:

* `limpar_rating`: converte avaliações numéricas em `float`.
* `limpar_data`: padroniza datas no formato `YYYY-MM-DD`.
* `limpar_execucoes`: remove formatações de texto (como vírgulas) e converte para `int`.
* `limpar_generos`: utiliza uma pilha iterativa para achatar listas de gêneros aninhadas e as retorna ordenadas alfabeticamente.

## Arquivos do projeto

* `catalogo.py`: classe `Catalogo` e funções auxiliares de limpeza de dados.
* `main.py`: processa o arquivo de consultas no modo batch.
* `cli.py`: interface interativa do menu via terminal.