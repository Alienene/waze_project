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

walls = [Wall(50, 50, 100, 10),
    Wall(170, 75, 10, 50),
    Wall(100, 175, 120, 10),
    Wall(50, 150, 10, 70),
    Wall(0, 370, 120, 10),
    Wall(170, 420, 200, 10),
    Wall(320, 370, 10, 100),
    Wall(370, 420, 100, 10),
    Wall(420, 470, 10, 70),
    Wall(470, 395, 70, 10),
    Wall(220, 100, 70, 10),
    Wall(220, 50, 10, 70),
    Wall(50, 320, 120, 10),
    Wall(95, 295, 10, 70),
    Wall(170, 270, 70, 10),
    Wall(270, 395, 170, 10),
    Wall(295, 270, 10, 70),
    Wall(370, 320, 70, 10),
    Wall(420, 295, 10, 70),
    Wall(120, 470, 70, 10),
    Wall(170, 445, 10, 70),
    Wall(50, 520, 170, 10),
    Wall(220, 495, 10, 70),
    Wall(320, 545, 120, 10),
    Wall(395, 520, 10, 70),
    Wall(470, 570, 70, 10),
    Wall(0, 620, 220, 10),
    Wall(170, 570, 10, 70),
    Wall(70, 595, 70, 10),
    Wall(520, 50, 120, 10),
    Wall(620, 75, 10, 70),
    Wall(570, 175, 120, 10),
    Wall(520, 150, 10, 70),
    Wall(470, 320, 170, 10),
    Wall(620, 370, 10, 120),
    Wall(670, 420, 120, 10),
    Wall(720, 470, 10, 70),
    Wall(770, 395, 70, 10),
    Wall(570, 100, 70, 10),
    Wall(570, 50, 10, 70),
    Wall(520, 320, 120, 10),
    Wall(545, 295, 10, 70),
    Wall(620, 270, 70, 10),
    Wall(720, 395, 170, 10),
    Wall(745, 270, 10, 70),
    Wall(820, 320, 70, 10),
    Wall(870, 295, 10, 70),
    Wall(570, 470, 70, 10),
    Wall(620, 445, 10, 70),
    Wall(520, 520, 170, 10),
    Wall(670, 495, 10, 70),
    Wall(770, 545, 120, 10),
    Wall(845, 520, 10, 70),
    Wall(920, 570, 70, 10),
    Wall(0, 0, 1220, 10),
    Wall(0, 0, 10, 620),
    Wall(1210, 0, 10, 620),
    Wall(0, 610, 1220, 10),
    Wall(320, 100, 170, 10),
    Wall(470, 170, 10, 120),
    Wall(320, 220, 170, 10),
    Wall(520, 50, 10, 170),
    Wall(570, 75, 120, 10),
    Wall(620, 120, 10, 120),
    Wall(470, 270, 220, 10),
    Wall(570, 320, 10, 120),
    Wall(620, 420, 220, 10),
    Wall(770, 50, 10, 120),
    Wall(720, 320, 10, 170),
    Wall(820, 370, 170, 10),
    Wall(920, 420, 10, 120),
    Wall(970, 470, 120, 10),
    Wall(1020, 520, 10, 120),
    Wall(1070, 220, 120, 10),
    Wall(1020, 120, 10, 120),
    Wall(970, 75, 70, 10),
    Wall(920, 145, 10, 95),
    Wall(870, 170, 70, 10),
    Wall(820, 195, 10, 120),
    Wall(770, 245, 70, 10),
    Wall(720, 270, 10, 70),
    Wall(670, 295, 70, 10),
    Wall(620, 245, 10, 70),
    Wall(570, 220, 70, 10),
    Wall(520, 245, 10, 120),
    Wall(470, 345, 70, 10),
    Wall(420, 370, 10, 70),
    Wall(370, 395, 70, 10),
    Wall(320, 370, 10, 70),
    Wall(270, 395, 70, 10),
    Wall(220, 345, 10, 70),
    Wall(170, 320, 70, 10),
    Wall(120, 370, 10, 120),
    Wall(70, 445, 70, 10),
    Wall(20, 470, 10, 120),
    Wall(420, 10, 10, 120)]

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