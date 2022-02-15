import pygame


class Bubble(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/bulles/Bulle_1.png')
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect() 
        self.rect.x = 420
        self.rect.y = 80
