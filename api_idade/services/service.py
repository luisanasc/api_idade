# -*- coding: utf-8 -*-
_pipeline = None  # guardará o pipeline carregado (com pré-processamento + modelo)

def carregar_artefatos(caminho_pipeline):
    """Carrega o pipeline serializado com cloudpickle (.pkl)."""
    # Imports locais
    import os
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
    import cloudpickle as cp
    global _pipeline
    with open(caminho_pipeline, "rb") as f:
        _pipeline = cp.load(f)

def prever_um(payload):
    """Converte o payload em DataFrame e executa predict no pipeline carregado."""
    # Imports locais
    import pandas as pd
    global _pipeline
    if _pipeline is None:
        raise RuntimeError("Pipeline não carregado. Verifique o evento de startup.")
    df = pd.DataFrame([payload])         # um único registro
    y_pred = _pipeline.predict(df)       # retorna array com 1 valor
    return float(y_pred[0])
