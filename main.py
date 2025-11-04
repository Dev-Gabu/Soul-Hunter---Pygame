import pygame
import os

from settings import LARGURA, ALTURA, FPS, PRETO, BRANCO
from souls import Fantasma
from utils import carregar_imagem

def spawn_fantasma():
    novo_fantasma = Fantasma(fantasma_img)
    todos_sprites.add(novo_fantasma)

# Inicialização
pygame.init()
pygame.mouse.set_visible(False)

TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Soul Hunter")

fantasma_img = carregar_imagem('fantasma.png', (160, 160))
fundo_img = carregar_imagem('background.png', (LARGURA, ALTURA))
frontal_img = carregar_imagem('foreground.png', (LARGURA, ALTURA))
mira_img = carregar_imagem('mira.png', (90, 90))
graves_img = carregar_imagem('graves.png', (LARGURA, ALTURA))

#Variáveis de controle do jogo
score = 0
fantasma_timer = 0
estado_spawn = "AGUARDANDO"
INTERVALO_SPAWN = FPS * 1 
tempo_ultimo_fantasma = 0

#Controle de jogo
clock = pygame.time.Clock()
rodando = True

todos_sprites = pygame.sprite.Group()
fantasma = Fantasma(fantasma_img)
todos_sprites.add(fantasma)

# Loop Principal do Jogo
while rodando:
    clock.tick(FPS)

    # Tratamento de Eventos 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicao_clique = evento.pos
            for fantasma in todos_sprites:
                if fantasma.rect.collidepoint(posicao_clique):
                 
                    score += 10 
                    print(f"Acertou! Pontuação: {score}")
                    fantasma.kill()
                    break

    todos_sprites.update()

    # B. Lógica de Spawn de Fantasmas
    if len(todos_sprites) == 0:
        if estado_spawn == "AGUARDANDO":
            tempo_ultimo_fantasma = pygame.time.get_ticks() 
            estado_spawn = "ESPERANDO"

        if estado_spawn == "ESPERANDO":
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - tempo_ultimo_fantasma > INTERVALO_SPAWN * (1000 / FPS):
                spawn_fantasma()
                estado_spawn = "AGUARDANDO"
    
    # D. Desenho/Renderização
    if fundo_img:
        TELA.blit(fundo_img, (0, 0)) 
    else:
        TELA.fill(PRETO) 

    todos_sprites.draw(TELA)

    if frontal_img:
        TELA.blit(frontal_img, (0, 0)) 

    if graves_img:
        TELA.blit(graves_img, (0, 0))

    fonte = pygame.font.Font(None, 36)
    texto_pontos = fonte.render(f"Almas: {score}", True, BRANCO)
    TELA.blit(texto_pontos, (10, 10))

    # Desenha a mira personalizada
    if mira_img:
        mira_rect = mira_img.get_rect()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mira_rect.center = (mouse_x, mouse_y)
        TELA.blit(mira_img, mira_rect)
    else:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        pygame.draw.circle(TELA, BRANCO, (mouse_x, mouse_y), 5, 1)

    pygame.display.flip()

# --- 7. Finalização ---
pygame.quit()