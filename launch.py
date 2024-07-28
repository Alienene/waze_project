import pygame
import animation
import math
pygame.init()

picture1 = pygame.image.load("background.png")
picture1 = pygame.transform.scale(picture1,(1200,650))


class Wall():
    def __init__(self,x=0,y=0,width=0,height=0,color=(22,26,31)):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)

walls = [Wall(350,250,200,10),
        Wall(275,300,150,10),
        Wall(250,275,50,10),
        Wall(125,250,50,25),
        Wall(0,200,50,20),
        Wall(100,120,75,10),
        Wall(250,0,50,15),
        Wall(375,0,25,25)]





window = pygame.display.set_mode((1200,650))
clock = pygame.time.Clock()
player = animation.Player((10,0))
game = True

while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    player.events(event)
    window.fill((0,0,0))
    window.blit(picture1,(0,0))
    
    

    window.blit(player.image, player.rect)
    for w in walls:
        w.fill()


    clock.tick(30)
    pygame.display.update()