import os
import pygame

from settings import PASTA_ASSETS

def carregar_imagem(nome_arquivo,tamanho=None):
    caminho = os.path.join(PASTA_ASSETS,'sprites', nome_arquivo)
    try:
        imagem = pygame.image.load(caminho).convert_alpha()
        if tamanho:
            imagem = pygame.transform.scale(imagem, tamanho)
        return imagem
    except pygame.error as e:
        print(f"Erro ao carregar imagem {nome_arquivo}: {e}")
        return None
    
def carregar_som(nome_arquivo):
    caminho = os.path.join(PASTA_ASSETS, 'sounds', nome_arquivo)
    try:
        som = pygame.mixer.Sound(caminho)
        return som
    except pygame.error as e:
        print(f"Erro ao carregar som {nome_arquivo}: {e}")
        return None