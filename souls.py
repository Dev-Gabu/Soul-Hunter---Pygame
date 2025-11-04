import pygame
import random
from settings import LARGURA, ALTURA, FPS

class Fantasma(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img if img else pygame.Surface((160,160))
        if not img:
            self.image.fill((200, 200, 200))
            
        self.rect = self.image.get_rect()
        
        self.rect.x = random.randrange(LARGURA - self.rect.width)
        self.rect.y = random.randrange(self.rect.height, ALTURA - self.rect.height)
        
        self.speed_x = random.choice([-2, 2])
        self.speed_y = 0 
        self.TEMPO_MAXIMO_VIDA = FPS * 3 
        self.contador_vida = 0

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left < 0 or self.rect.right > LARGURA:
            self.speed_x *= -1

        self.contador_vida += 1
        if self.contador_vida >= self.TEMPO_MAXIMO_VIDA:
            self.kill()