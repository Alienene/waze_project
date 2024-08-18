import pygame
import random
from enemy import Enemy, bullets
from animation import walls, window, player
pygame.init()
f = pygame.font.Font(None,30) 
picture1 = pygame.image.load("background1.png")
picture1 = pygame.transform.scale(picture1,(1200,650))

clock = pygame.time.Clock()
enemy1 = Enemy(320, 490, 160, 100, 'enemy.png')
game = True

# class Player(pygame.sprite.Sprite):
#     def __init__(self, position):
#         self.sheet = pygame.image.load('enemie1.png')
life = 3
zminna = 0
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
    zminna += 1
    if zminna == 40:
        enemy1.shoot()
        zminna = 0
    l_bool = True
    for bullet in bullets:
        bullet.move()
        pygame.draw.rect(window, (255, 0, 0), bullet.rect)
        if player.rect.colliderect(bullet.rect):  
            life -= 1
            bullets.remove(bullet)
        for w in walls:
            if w.rect.colliderect(bullet.rect):
                bullets.remove(bullet)
        if life == 0: 
            game = False  

    
    time_text = f.render(f'Життя: {life} ', True, (255,225,25)) 
    window.blit(time_text,(10,10)) 

    clock.tick(30)
    pygame.display.update()