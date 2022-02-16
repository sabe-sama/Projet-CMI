import pygame

is_happy = True


class Bob(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        if is_happy:
            self.image = pygame.image.load('assets/LeMecQuiParle.png')
        else:
            self.image = pygame.image.load('assets/sad.JPEG')
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect() 
        self.rect.x = 300
        self.rect.y = 180


class WinButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/Win_button.png')
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect()


class WinButton2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/Win_button.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 190


class LoseButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/Lose_button.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = 690
        self.rect.y = 450


class LoseButton2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/Lose_button.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 130


class LoseButton3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/Lose_button.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 330


class LoseButton4(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/Lose_button.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = 430
        self.rect.y = 400


class LoseButton5(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/Lose_button.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 570
        self.rect.y = 190


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
