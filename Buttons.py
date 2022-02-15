from turtle import onclick
from typing_extensions import Self
import pygame

is_happy =True
class Bob(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.maxhealth = 1000
        self.health = 1000 
        if (is_happy) : 
            self.image = pygame.image.load('assets/LeMecQuiParle.png')
        else : 
            self.image = pygame.image.load('assets/sad.JPEG')
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect() 
        self.rect.x = 300
        self.rect.y = 180

class Win_Button(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/Win_button.png')
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect()

class Lose_Button(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/Lose_button.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = 690
        self.rect.y = 450