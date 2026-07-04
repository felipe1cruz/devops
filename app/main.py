from fastapi import FastAPI
from datetime import datetime

import requests

LISTA_TAREFAS = []
APP = FastAPI()

def nova_tarefa(id: int, titulo: str, descricao: str, concluido: bool):
    return {
        "id": id,
        "titulo": titulo,
        "descricao": descricao,
        "concluido": False,
        "criado_em": datetime.now()
    }

def verificar_existencia_tarefa(id: int):
    for tarefa in LISTA_TAREFAS:
        if id == tarefa['id']:
            return True
    return False

@APP.get("/")
def index():
    return "Olá, DevOps!"

@APP.get("/tarefas")
def listar_tarefas():
    if len(LISTA_TAREFAS) == 0:
        return LISTA_TAREFAS
    
    tarefas = []

    for tarefa in LISTA_TAREFAS:
        info = {"id": tarefa['id'], "titulo": tarefa['titulo']}
        tarefas.append(info)
        
    return tarefas

@APP.get("/tarefas/{id}")
def listar_tarefa_especifica(id: int):
    mensagem_padrao = {"mesnagem": "Não existe nenhuma tarefa"}
    if len(LISTA_TAREFAS) == 0:
        return mensagem_padrao

    if id >= 0 and id < len(LISTA_TAREFAS):
        return LISTA_TAREFAS[id]

    return mensagem_padrao

@APP.post("/tarefas")
def incluir_tarefa(id: int, titulo: str, descricao: str):
    tarefa_existe = verificar_existencia_tarefa(id)
    global LISTA_TAREFAS
    if tarefa_existe:
        return {"mensagem": "TAREFA JÁ EXISTE"}

    for tarefa in LISTA_TAREFAS:
        if tarefa is not None and tarefa["id"] == id:
            return "TAREFA JÁ EXISTE"
            
    nova = nova_tarefa(id, titulo, descricao, False)

    LISTA_TAREFAS.append(nova)

    return {"mensagem": "OK"}

    _
@APP.put("/tarefas/{id}")
def atualizar_tarefa(id: int, titulo: str = "", descricao: str = "", concluido: bool = False):
    global LISTA_TAREFAS

    # 1. Verifica se a tarefa existe
    tarefa_existe = verificar_existencia_tarefa(id)
    if not tarefa_existe:
        return {"mensagem": "TAREFA NÃO EXISTE!"}
    
    # 2. Busca o índice real da tarefa
    indice_alvo = -1
    for indice, tarefa in enumerate(LISTA_TAREFAS):
        if tarefa['id'] == id:
            indice_alvo = indice
            break
    
    # 3. Atualiza os dados se eles foram enviados
    if titulo != "":
        LISTA_TAREFAS[indice_alvo]['titulo'] = titulo
    
    if descricao !=  "":
        LISTA_TAREFAS[indice]['descricao'] = descricao
    
    if concluido == True:
        requests.post(
            "http://127.0.0.1:8000/notificar", 
            params={
                "titulo": LISTA_TAREFAS[indice_alvo]['titulo'], 
                "data_finalizacao": str(datetime.now())
            },
            timeout=10  # <-- ADICIONE ESTA LINHA
        )
        
        # Usando 127.0.0.1 é mais seguro que localhost para evitar o Erro 404 falso
        requests.post(
            "http://127.0.0.1:8000/notificar", 
            params={
                "titulo": LISTA_TAREFAS[indice_alvo]['titulo'], 
                "data_finalizacao": str(datetime.now())
            }
        )

    return {"mensagem": "OK"}


@APP.delete("/tarefas/{id}")
def deletar_tarefa(id: int):
    global LISTA_TAREFAS

    tarefa_existe = verificar_existencia_tarefa(id)

    if not tarefa_existe:
        return {"mensagem": "TAREFA NÃO EXISTE"}

        tarefa = None
    for indice in range(len(LISTA_TAREFAS)):
        tarefa = LISTA_TAREFAS[indice]

        # Sai do loop
        if tarefa['id'] == id:
            break
    
    LISTA_TAREFAS.pop(indice)

    return {"mensagem": "OK"}    