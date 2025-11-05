import pygame
import random
from settings import LARGURA, ALTURA, FPS
from utils import carregar_som
import math

class Fantasma(pygame.sprite.Sprite):

    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.som_escape = carregar_som('pop-effect.wav')
        
        self.original_image = img if img else pygame.Surface((160,160))
        if not img:
            self.original_image.fill((200, 200, 200)) 
            
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()

        # Parâmetros da Onda
        self.amplitude_y = random.uniform(5, 50)
        self.frequencia_y = random.uniform(0.005, 0.002)
        self.fase = random.uniform(0, 2 * math.pi)
        self.velocidade_horizontal = random.choice([-1, 1]) * random.uniform(1.5, 3.5)
        
        min_y = ALTURA // 3 
        max_y = ALTURA - self.rect.height
        
        self.x = float(random.randrange(LARGURA - self.rect.width))
        self.y = float(random.randrange(min_y, max_y)) 
        
        self.rect.topleft = (int(self.x), int(self.y))
        
        self.TEMPO_MAXIMO_VIDA = FPS * 5 
        self.contador_vida = 0

    def ajustar_escala(self):
        
        min_y = ALTURA // 3 
        max_y = ALTURA - 50
        
        if self.y < min_y:
            fator_y = 0 
        elif self.y > max_y:
            fator_y = 1
        else:
            fator_y = (self.y - min_y) / (max_y - min_y)
            
        escala_min = 0.7 
        escala_max = 1.3
        
        escala_atual = escala_min + (escala_max - escala_min) * fator_y
        
        novo_tamanho = (int(self.original_image.get_width() * escala_atual),
                        int(self.original_image.get_height() * escala_atual))
                        
        self.image = pygame.transform.scale(self.original_image, novo_tamanho)
        
        centro = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = centro

    def update(self):
        self.x += self.velocidade_horizontal
        if self.x <= 0 or self.x + self.rect.width >= LARGURA:
            self.velocidade_horizontal *= -1
        
        self.y += self.amplitude_y * self.frequencia_y * math.cos(self.fase) 
        self.fase += self.frequencia_y * 10
        
        if self.fase > 2 * math.pi:
            self.fase -= 2 * math.pi 

        self.ajustar_escala() 
        self.rect.topleft = (int(self.x), int(self.y))

        self.contador_vida += 1
        if self.contador_vida >= self.TEMPO_MAXIMO_VIDA:
            if self.som_escape:
                self.som_escape.play()
            self.kill()