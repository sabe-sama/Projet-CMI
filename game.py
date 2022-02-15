# création d'une classe qui va représenter le jeu
import pygame


class Game:
    def __init__(self):
        # définir si le jeu a commencé ou non
        self.is_playing = False


class GameOver(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/GameOver.JPEG')
        self.image = pygame.transform.scale(self.image, (720, 480))
        self.rect = self.image.get_rect()
