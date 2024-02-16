# au préhalable installer la bibliotheque pygame avec :
# pip install pygame
import pygame

pygame.init()
# declarations de mes variables
fenetre = pygame.display.set_mode((640,480))

background = pygame.image.load("./assets/img/background.jpg").convert()
goomba = pygame.image.load("./assets/img/goomba.png").convert_alpha()
mario = pygame.image.load("./assets/img/mario.png").convert_alpha()
fantome = pygame.image.load("./assets/img/fantome.png").convert_alpha()
# importer le son
sound = pygame.mixer.Sound("./assets/audio/miaou.mp3")
# fonction de collision avec mario
def mario_collision (left,top):
   global mario, mario_rect
   print(f"position goomba left : {left}")
   print(f"position goomba top : {top}")
   if left<50 and top<70:
      print("Mario et mort")
      mario = pygame.image.load("./assets/img/fantome.png")

goomba_rect = goomba.get_rect()
goomba_rect.topleft = (320,240)
mario_rect = mario.get_rect()
mario_rect.topleft = (0,0)

fenetre.blit(background,(0,0))
# je crée une boucle 
continuer = True
while (continuer) :
   for event in pygame.event.get() :
      if event.type == pygame.KEYDOWN :
         # print(event.key)
         if event.key == 27 : # touche Escape
            continuer = False
            
         if event.key == 100 : # Touche D deplacement à droite
            if goomba_rect.left < 500 :
               goomba_rect = goomba_rect.move(25,0)
               mario_collision (goomba_rect.left,goomba_rect.top)
            else :
               sound.play()
         if event.key == 113 : # Touche Q deplacement à gauche
            if goomba_rect.left > 0 :
               goomba_rect = goomba_rect.move(-25,0)
               mario_collision (goomba_rect.left,goomba_rect.top)
            else :
              sound.play()
         if event.key == 115 : # Touche S deplacement bas
            if goomba_rect.top < 380 :
               goomba_rect = goomba_rect.move(0,25)
               mario_collision (goomba_rect.left,goomba_rect.top)
            else :
               sound.play()
         if event.key == 122 : # Touche Z deplacement haut
            if goomba_rect.top > 0 :
               goomba_rect = goomba_rect.move(0,-25)
               mario_collision (goomba_rect.left,goomba_rect.top)
            else :
               sound.play()

   fenetre.blit(background,(0,0))
   fenetre.blit(goomba,goomba_rect)
   fenetre.blit(mario,mario_rect)
   pygame.display.update()

pygame.quit() 
