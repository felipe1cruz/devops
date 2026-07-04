from fastapi import FastAPI

APP_NOTIFICACAO = FastAPI()
    
# Criar uma rota para receber tarefa finalizada
# APP_NOTIFICACAO.post("/notificar")
# Entrada:
#   - Recebe título da tarefa e data de finalização da tarefa
# Saída:
#   - print no terminal
@APP_NOTIFICACAO.post("/notificar")
def notificar_tarefa_finalizada(titulo: str, data_finalizacao: str):
    print(f"Tarefa finalizada: {titulo}, Data de finalização: {data_finalizacao}")
    return {"mensagem": "Notificação recebida com sucesso!"}



