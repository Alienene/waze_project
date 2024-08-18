import pygame
from enemy import Enemy
from animation import walls, window, player
pygame.init()

picture1 = pygame.image.load("background1.png")
picture1 = pygame.transform.scale(picture1,(1200,650))

clock = pygame.time.Clock()
enemy1 = Enemy(50, 550, 150, 100, 'enemie1.png')
game = True

# class Player(pygame.sprite.Sprite):
#     def __init__(self, position):
#         self.sheet = pygame.image.load('enemie1.png')


while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    player.events(event)
    window.fill((0,0,0))
    window.blit(picture1,(0,0))
    
    window.blit(player.image, player.rect)
    window.blit(enemy1.image, (enemy1.rect.x, enemy1.rect.y))  
    for w in walls:
        w.fill()


    clock.tick(30)
    pygame.display.update()