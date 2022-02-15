# On importe les modules dont nous avons besoin. 
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
pygame.display.set_caption("GG EZ")

# On définit la taille de la fenêtre, que l'on insère dans la variable .
screen = pygame.display.set_mode((720, 480))
# myfont = pygame.font.SysFont('Helvetic', 20)

# On charge un fond d'écran et on le redimensionne.
background = pygame.image.load('assets/bg.png')
background = pygame.transform.scale(background, (720, 480))


# On charge Bob.
bob = Bob()
# On charge les bouttons "Plau","gagner" et "perdre".
win_button = WinButton()
lose_button = LoseButton()
p_button = PlayButton()
# On charge les bulles.
bulle_1 = Bubble()

titlescreen = True
# On crée la varible "running". Elle vaut "True" tant quand le jeu tourne. 
running = True
# Cette variable nous sert à initier une boucle while, qui nous permet de faire tourner le jeu.  
gameOver = GameOver()


def show_game_over():
    global titlescreen, win
    screen.blit(gameOver.image, gameOver.rect)
    pygame.display.flip()
    time.sleep(1)
    titlescreen = True
    win = False


win = False

while running:
    pygame.mouse.set_visible(True)
    
    if not win:
        while titlescreen:
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
    screen.blit(bob.image, bob.rect)
    # On affiche les bouttons "gagner" et "perdre".
    screen.blit(win_button.image, win_button.rect)
    screen.blit(lose_button.image, lose_button.rect)
    # On affiche les bulles.
    screen.blit(bulle_1.image, bulle_1.rect)
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
        if win:
            show_game_over()
