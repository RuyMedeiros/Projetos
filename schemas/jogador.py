def jogadorEntidade(db_item) -> dict:
    return {
    "id": str(db_item['_id']),
    "nome": db_item['jogador_nome'],
    "idade": db_item['jogador_idade'],
    "time": db_item['jogador_time']
    }

def listaJogadoresEntidade(db_item_lista) -> list:
    lista_jogadores = []
    for item in db_item_lista:
        lista_jogadores.append(jogadorEntidade(item))
    return lista_jogadores