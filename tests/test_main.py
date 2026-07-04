from fastapi.testclient import TestClient

from app import APP

CLIENT = TestClient(APP)

def test_index():
    requisicao = CLIENT.get("/")

    assert requisicao.status_code == 200
    assert requisicao.json() == "Olá, DevOps!"

def test_criar_tarefa_com_sucesso():
    dados_tarefa = {
        "id": 1,
        "titulo": "Aprender Testes",
        "descricao": "Criar testes unitários com Pytest e FastAPI"
    }

    requisicao = CLIENT.post("/tarefas", params=dados_tarefa)

    assert requisicao.status_code == 200
    assert requisicao.json() == {"mensagem": "OK"}

def test_criar_tarefa_ja_existente():
    dados_tarefa = {
        "id": 2,
        "titulo": "Tarefa Duplicada",
        "descricao": "Testando a duplicidade"
    }

    CLIENT.post("/tarefas", params=dados_tarefa)

    requisicao = CLIENT.post("/tarefas", params=dados_tarefa)

    assert requisicao.status_code == 200
    assert requisicao.json() == {"mensagem": "TAREFA JÁ EXISTE"}

