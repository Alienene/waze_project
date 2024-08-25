import pygame
import random
from enemy import Enemy, bullets
from animation import walls, window, player
pygame.init()
f = pygame.font.Font(None,30) 
picture1 = pygame.image.load("background1.png")
picture1 = pygame.transform.scale(picture1,(1200,650))

pygame.mixer.music.load('background_music.mp3')

star_collect = pygame.mixer.Sound('star_collect.mp3')

receiving_damage = pygame.mixer.Sound('damage.mp3')

star_image = pygame.image.load('star.png')
star_image = pygame.transform.scale(star_image, (65, 65))

stars = [(350, 410), (940, 430), (590, 190)]

collected_stars = 0

heart_image = pygame.image.load('heart.png')
heart_image = pygame.transform.scale(heart_image, (40, 40))

clock = pygame.time.Clock()
enemy1 = Enemy(320, 490, 160, 100, 'enemy.png')
game = True
pygame.mixer.music.play(-1)

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
            pygame.mixer.Sound.play(receiving_damage)
            bullets.remove(bullet)
        for w in walls:
            if w.rect.colliderect(bullet.rect):
                bullets.remove(bullet)
        if life == 0: 
            game = False 
        for star in stars[:]:
            if player.rect.colliderect(pygame.Rect(star[0], star[1], star_image.get_width(), star_image.get_height())):
                stars.remove(star)
                collected_stars += 1
        
                

    for star in stars:
        window.blit(star_image, star)

    for i in range(collected_stars):
        window.blit(star_image, (1050 + i * 40, 7))

    for i in range(life):
        window.blit(heart_image, (10 + i * (heart_image.get_width() + 5), 10))

   

    

    clock.tick(30)
    pygame.display.update()