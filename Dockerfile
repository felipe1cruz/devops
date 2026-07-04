FROM python:3.12-slim

RUN mkdir app/

WORKDIR app/

COPY requirements.txt .
COPY app/main.py .

RUN pip install -r requirements.txt

CMD ["fastapi", "run"]

# 1. Construir imagem Docker (docker build)
# 2. Executar contêiner com base na imagem (mapear porta 8000 do container para 80 do host)
# 3. Tornar a porta 80 como pública
# 4. Acessar página no navegador para testar