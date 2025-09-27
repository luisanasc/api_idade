# -*- coding: utf-8 -*-
def carregar_artefato(caminho):
    import cloudpickle as cp
    with open(caminho, "rb") as f:
        return cp.load(f)
