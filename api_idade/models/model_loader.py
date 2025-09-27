# -*- coding: utf-8 -*-
# Módulo mantido por compatibilidade; não utilizado no fluxo atual.
def carregar_modelo(caminho_modelo):
    import cloudpickle as cp
    with open(caminho_modelo, "rb") as f:
        return cp.load(f)
