# -*- coding: utf-8 -*-
def criar_app():
    # Imports locais (carregados somente quando a API sobe)
    from fastapi import FastAPI, Body
    from api_idade.services.service import carregar_artefatos, prever_um

    # Caminho do pipeline dentro do pacote (execução a partir da raiz do projeto)
    CAMINHO_PIPELINE = "api_idade/artefatos/pipeline_referencia.pkl"

    app = FastAPI(title="API de Previsão de Idade")

    @app.on_event("startup")
    def iniciar():
        # Carrega pipeline único (pré-processamento + modelo + normalização do alvo)
        carregar_artefatos(caminho_pipeline=CAMINHO_PIPELINE)

    @app.get("/health")
    def verificar():
        return {"status": "ok"}

    @app.post("/predict")
    def prever(payload: dict = Body(..., description="JSON com as chaves de entrada")):
        # payload -> dict com as colunas de entrada (iguais às do treino)
        idade_prevista = prever_um(payload)
        return {"idade_prevista": idade_prevista}

    return app

# Instância padrão para uvicorn:  uvicorn api_idade.main:app --reload --host 127.0.0.1 --port 8010
app = criar_app()
