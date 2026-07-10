from fastapi.testclient import TestClient

from app import APP

CLIENT = TestClient(APP)

def criar_tarefa_mock():
    requisicao = CLIENT.post("/tarefas?id=0&titulo=tarefa&descricao=descricao-tarefa")

def test_index():
    requisicao = CLIENT.get("/")

    assert requisicao.status_code == 200
    assert requisicao.json() == "Olá, DevOps!"

# Criar um teste unitário para validar se a tarefa foi criada com sucesso
# CLIENT.post(...) (substituir pela string para criação de tarefa)
# Verificar se o código de status é 201
# Verificar se o retorno, quando tarefa é criada, é igual a {"mensagem": "OK"} ou conforme definido na sua API
# Verificar se o retorno, quando a tarefa já existe, é igual a {"mensagem" : "TAREFA JÁ EXISTE"} ou conforme definido na sua API

def test_criar_tarefa():
    requisicao = CLIENT.post("/tarefas?id=0&titulo=tarefa&descricao=descricao-tarefa")

    assert requisicao.status_code == 201
    assert requisicao.json() == {"mensagem": "OK"}

    requisicao = CLIENT.post("/tarefas?id=0&titulo=tarefa&descricao=descricao-tarefa")
    assert requisicao.status_code == 202
    assert requisicao.json()['detail'] == {"mensagem": "TAREFA JÁ EXISTE!"}

def test_remover_tarefa():
    criar_tarefa_mock()

    requisicao = CLIENT.delete("/tarefas/0")
    assert requisicao.status_code == 200
    assert requisicao.json() == {"mensagem": "OK"}

    requisicao = CLIENT.delete("/tarefas/10")
    assert requisicao.status_code == 200
    assert requisicao.json() == {"mensagem": "TAREFA NÃO EXISTE"}

def test_atualizar_tarefa():
    criar_tarefa_mock()

    requisicao = CLIENT.put("/tarefas/0?id=0&titulo=tarefa_mock")
    assert requisicao.status_code == 200
    assert requisicao.json() == {"mensagem": "OK"}

    requisicao = CLIENT.get("/tarefas/0")
    assert requisicao.status_code == 200
    assert requisicao.json()["titulo"] == "tarefa_mock"

def test_verificar_tarefa_especifica():
    criar_tarefa_mock()
    requisicao = CLIENT.get("/tarefas/0")

    assert requisicao.status_code == 200

    dados = requisicao.json()
    assert dados["titulo"] == "tarefa_mock"
    assert dados["descricao"] == "descricao-tarefa"
    assert dados["id"] == 0
    assert dados["concluido"] == False

    requisicao = CLIENT.get("/tarefas/5")

    assert requisicao.json() == {"mensagem": "Não existe nenhuma tarefa"}

def test_metricas():
    # 1. Garante que temos um cenário limpo/controlado.
    CLIENT.delete("/tarefas/0")
    CLIENT.delete("/tarefas/1")
    
    # 2. Testa o cenário com a lista vazia (0 tarefas)
    requisicao = CLIENT.get("/metricas")
    assert requisicao.status_code == 200
    assert requisicao.json() == {
        "quantidade_tarefas": 0,
        "tarefas_finalizadas": 0,
        "tarefas_pendentes": 0
    }

    CLIENT.post("/tarefas?id=0&titulo=Tarefa1&descricao=Teste")
    
    requisicao = CLIENT.get("/metricas")
    assert requisicao.status_code == 200
    assert requisicao.json() == {
        "quantidade_tarefas": 1,
        "tarefas_finalizadas": 0,
        "tarefas_pendentes": 1
    }

def test_health():
    requisicao = CLIENT.get("/health")
    
    # 1.1 Retornar status_code 200
    assert requisicao.status_code == 200
    
    # 1.2 Retornar {"status": "OK"}
    assert requisicao.json() == {"status": "OK"}
    
