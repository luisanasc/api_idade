# Imagem base oficial do Python (leve)
FROM python:3.12-slim

# Variáveis de ambiente: não gerar .pyc, logs sem buffer, silenciar avisos do TensorFlow
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TF_CPP_MIN_LOG_LEVEL=3

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia apenas as dependências e instala (camada estável reaproveitada pelo cache)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto preservando o pacote 'api_idade' visível para o Python
COPY . /app/api_idade

# Porta interna onde o Uvicorn escuta
EXPOSE 8010

# Comando para iniciar a API quando o container subir
CMD ["uvicorn", "api_idade.main:app", "--host", "0.0.0.0", "--port", "8010"]
