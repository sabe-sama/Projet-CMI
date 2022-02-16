# On importe les modules dont nous avons besoin.
import pygame.event
# On importe également le contenu de nos autres fichiers relatifs au jeu.
from Buttons import *
from bulles import *
from bob import *
# On initialise ce que l'on a récuppéré dans le module pygame.
pygame.init()

# On génere la fenêtre du jeu.
pygame.font.init()

# On définit le titre de la fenêtre.
pygame.display.set_caption("EZ WIN")

# On définit la taille de la fenêtre, que l'on insère dans la variable .
screen = pygame.display.set_mode((720, 480))

# On charge un fond d'écran et on le redimensionne.
background = pygame.image.load('assets/bg.png')
background = pygame.transform.scale(background, (720, 480))


# On défini des variables associées aux class bob.
bob = Bob()
sad_bob = SadBob()
uncanny_bob = UncannyBob()
# On defini des variables associés à tout les différents boutons du jeu.
win_button = WinButton()
lose_button = LoseButton()
p_button = PlayButton()
replay_button = ReplayButton()
quit_button = QuitButton()
# On défini des variables associées aux bulles qu'utilisera bob.
bubble_1 = Bubble1()
bubble_2 = Bubble2()
bubble_3 = Bubble3()
# On crée la varible "running". Elle vaut "True" tant quand le jeu tourne. 
running = True
# Cette variable nous sert à initier une boucle while, qui nous permet de faire tourner le jeu.

titlescreen = True
sadness = 0


def show_game_over():
    """on créer une fonction qui apparaitra à chaque fois que le joueur perd
    pour l'appeller plus facilement"""
    global titlescreen, win, running, event
    run = True
    while run:
        bg = pygame.image.load('assets/bob/GameOver.png')
        bg = pygame.transform.scale(bg, (720, 480))
        screen.blit(bg, (0, 0))
        screen.blit(replay_button.image, replay_button.rect)
        screen.blit(quit_button.image, quit_button.rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # vérfication si la souris a touché le bouton rejouer
                if quit_button.rect.collidepoint(event.pos):
                    run = False
                    running = False
                    pygame.quit()
                if replay_button.rect.collidepoint(event.pos):
                    win = False
                    titlescreen = True
                    run = False


win = False

while running:
    pygame.mouse.set_visible(True)
    
    if not win:
        while titlescreen:
            sadness = 0
            background = pygame.image.load('assets/1.JPEG')
            background = pygame.transform.scale(background, (720, 480))
            screen.blit(background, (0, 0))
            screen.blit(p_button.image, p_button.rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # vérfication si la souris a touché le bouton play
                    if p_button.rect.collidepoint(event.pos):
                        titlescreen = False

    background = pygame.image.load('assets/bg.png')
    background = pygame.transform.scale(background, (720, 480))

    screen.blit(background, (0, 0))
    # On affiche Bob.
    if sadness == 0:
        screen.blit(bob.image, bob.rect)
        screen.blit(bubble_1.image, bubble_1.rect)
    elif sadness == 1:
        screen.blit(sad_bob.image, sad_bob.rect)
        screen.blit(bubble_2.image, bubble_2.rect)
    elif sadness == 2:
        screen.blit(uncanny_bob.image, uncanny_bob.rect)
        screen.blit(bubble_3.image, bubble_3.rect)

    # On affiche les bouttons "gagner" et "perdre".
    screen.blit(win_button.image, win_button.rect)
    screen.blit(lose_button.image, lose_button.rect)
    # On affiche les bulles.
    # mettre à jour l'écran
    pygame.display.flip()
    # applique le bouton qui démarre le jeu
    # screen.blit(play_button, play_button_rect)
    # si le joueur ferme la fenetre

    for event in pygame.event.get():
        # que l'evenemenet est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # vérfication si la souris a touché le bouton play
            if win_button.rect.collidepoint(event.pos):
                # mettre le jeu en mode lancer
                # Game.is_playing = True
                win = True
            if lose_button.rect.collidepoint(event.pos):
                sadness += 1
                if sadness == 0:
                    screen.blit(bob.image, bob.rect)
                    screen.blit(bubble_1.image, bubble_1.rect)
                elif sadness == 1:
                    screen.blit(sad_bob.image, sad_bob.rect)
                    screen.blit(bubble_2.image, bubble_2.rect)
                elif sadness == 2:
                    screen.blit(uncanny_bob.image, uncanny_bob.rect)
                    screen.blit(bubble_3.image, bubble_3.rect)
                pygame.display.flip()

        if win:
            show_game_over()
