import pygame


class Bubble1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/bulles/Bulle_1.png')
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 420
        self.rect.y = 80


class Bubble2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/bulles/Bulle_2.png')
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 420
        self.rect.y = 80


class Bubble3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/bulles/Bulle_3.png')
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect() 
        self.rect.x = 420
        self.rect.y = 80


class BubbleLv1Part2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/bulles/Bulle_lv1part2.png')
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = 420
        self.rect.y = 0
