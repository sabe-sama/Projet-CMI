import pygame

is_happy = True


class WinButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/Win_button.png')
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect()


class LoseButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/Lose_button.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = 690
        self.rect.y = 450


<<<<<<< Updated upstream
=======
class LoseButton5(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/Lose_button.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 570
        self.rect.y = 190


>>>>>>> Stashed changes
class PlayButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/play_button.png')
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect()
        self.rect.x = 210
        self.rect.y = 90


class ReplayButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/rejouer.png')
        self.image = pygame.transform.scale(self.image, (200, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 300


class QuitButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/quitter.png')
        self.image = pygame.transform.scale(self.image, (200, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 300
