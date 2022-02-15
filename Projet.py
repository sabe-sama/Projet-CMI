# On importe les modules dont nous avons besoin. 
import pygame
import math
import time
# On importe également le contenu de nos autres fichiers relatifs au jeu.
from game import *
from Buttons import *
from bulles import *
# On initialise ce que l'on a récuppéré dans le module pygame.
pygame.init()

# On génere la fenêtre du jeu.
pygame.font.init()

# On définit le titre de la fenêtre.
pygame.display.set_caption("the sympathetic game")

# On définit la taille de la fenêtre, que l'on insère dans la variable .
screen = pygame.display.set_mode((720,480))
#myfont = pygame.font.SysFont('Helvetic', 20)

# On charge un fond d'écran et on le redimensionne.
background = pygame.image.load('assets/bg.png')
background = pygame.transform.scale(background, (720, 480))


# On charge Bob.
bob = Bob()
# On charge les bouttons "gagner" et "perdre".
win_Button = Win_Button()
lose_Button = Lose_Button()
# On charge les bulles.
Bulle_1 = Bubble()


# On crée la varible "running". Elle vaut "True" tant quand le jeu tourne. 
running=True
# Cette variable nous sert à initier une boucle while, qui nous permet de faire tourner le jeu.  
win = False
while running:
    pygame.mouse.set_visible(1)
    if not (win):
        # On applique le background du jeu.
        screen.blit(background, (0,0))

        # On affiche Bob.
        screen.blit(bob.image, bob.rect)
        # On affiche les bouttons "gagner" et "perdre".
        screen.blit(win_Button.image, win_Button.rect)
        screen.blit(lose_Button.image, lose_Button.rect)
        # On affiche les bulles.
        screen.blit(Bulle_1.image, Bulle_1.rect) 


    #mettre à jour l'écran
    pygame.display.flip()

    #applique le bouton qui démarre le jeu
    #screen.blit(play_button, play_button_rect)


    #si le joueur ferme la fenetre
    for event in pygame.event.get():
        #que l'evenemenet est fermeture de fenetre
        if event.type== pygame.QUIT:
            running=False
            pygame.quit
        
        
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            #vérfication si la souris a touché le bouton play
            if win_Button.rect.collidepoint(event.pos):
        #        #mettre le jeu en mode lancer
        #        Game.is_playing = True
                win = True

        if (win):
            gameOver = GameOver()
            screen.blit(gameOver.image, gameOver.rect)
            pygame.display.flip()
            time.sleep(5)
            win = False