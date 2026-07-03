from fastapi import FastAPI
from datetime import datetime


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

@APP.get("/")
def index():
    return "Olá, DevOps!"

@APP.get("/tarefas")
def listar_tarefas():
    if len(LISTA_TAREFAS) == 0:
        return LISTA_TAREFAS
    
    tarefas = []

    for tarefa in LISTA_TAREFAS:
        info = {"id": tarefa['id'], "titulo": taerfa['titulo']}
        tarefas.append(info)
        
    return tarefas
    