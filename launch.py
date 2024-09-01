import pygame
from enemy import Enemy, bullets
pygame.init()
f = pygame.font.Font(None,30) 
picture1 = pygame.image.load("background1.png")
picture1 = pygame.transform.scale(picture1,(1200,650))

pygame.mixer.music.load('background_music.mp3')

star_collect = pygame.mixer.Sound('star_collect.mp3')

receiving_damage = pygame.mixer.Sound('damage.mp3')
pygame.mixer.music.set_volume(2)

star_image = pygame.image.load('star.png')
star_image = pygame.transform.scale(star_image, (65, 65))

window = pygame.display.set_mode((1200,650))
class Wall():
    def __init__(self,x=0,y=0,width=0,height=0,color=(22,26,31)):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)

walls = [
    Wall(150, 50, 10, 250),    
    Wall(150, 300, 300, 10),   
    Wall(440, 50, 10, 250),    
    Wall(440, 50, 250, 10),    
    Wall(690, 50, 10, 250),    
    Wall(550, 300, 150, 10),   
    Wall(840, 50, 10, 150),    
    Wall(840, 200, 250, 10),   
    Wall(1090, 50, 10, 150),   
    Wall(150, 400, 300, 10),   
    Wall(150, 400, 10, 150),   
    Wall(440, 400, 10, 250),   
    Wall(550, 400, 150, 10),   
    Wall(690, 400, 10, 250),  
    Wall(840, 400, 250, 10),   
    Wall(1090, 400, 10, 150),
    Wall(550, 150, 10, 150),
    Wall(840, 410, 10, 150),
    Wall(840, 150, 10, 150),
    Wall(940, 300, 10, 100)
]



class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        self.sheet = pygame.image.load('player2.png')
        self.sheet.set_clip(pygame.Rect(0,0,48,69))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0 # рамка
        self.down = {
    0: (12, 0, 45, 63), 
    1: (77, 0, 45, 63), 
    2: (142, 0, 45, 63),
    3: (207, 0, 45, 63)
}
        self.left = {
    0: (12, 63, 45, 63), 
    1: (77, 63, 45, 63), 
    2: (142, 63, 45, 63),
    3: (207, 63, 45, 63)
}
        self.right = {
    0: (12, 126, 45, 63), 
    1: (77, 126, 45, 63), 
    2: (142, 126, 45, 63),
    3: (207, 126, 45, 63)
}
        self.up = {
    0: (12, 189, 45, 63), 
    1: (77, 189, 45, 63), 
    2: (142, 189, 45, 63),
    3: (207, 189, 45, 63)
}



        


        
    def update_frame(self, frame_set): # ф-ція для перебору спрайтів 
        self.frame += 1
        if self.frame > (len(frame_set)-1):
            self.frame = 0
        return frame_set[self.frame]


    def clip(self, clip_rect):
        if type(clip_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.update_frame(clip_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clip_rect))
        return clip_rect
    
    def update(self, direction):
        if direction == "down":
            self.clip(self.down)
            self.rect.y += 20
            for w in walls:
                if player.rect.colliderect(w.rect):
                    player.rect.bottom = w.rect.top
        if direction == "left":
            self.clip(self.left)
            self.rect.x -= 20
            for w in walls:
                if player.rect.colliderect(w.rect):
                    player.rect.left = w.rect.right
        if direction == "right":
            self.clip(self.right)
            self.rect.x += 20
            for w in walls:
                if player.rect.colliderect(w.rect):
                    player.rect.right = w.rect.left
        if direction == "up":
            self.clip(self.up)
            self.rect.y -= 20
            for w in walls:
                if player.rect.colliderect(w.rect):
                    player.rect.top = w.rect.bottom

        
        if direction == "stand_down":
            self.clip(self.down[0])
        if direction == "stand_left":
            self.clip(self.left[0])
        if direction == "stand_right":
            self.clip(self.right[0])
        if direction == "stand_up":
            self.clip(self.up[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())


    def events(self, event):
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_UP:
                self.update('up')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_DOWN:
                self.update('down')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.update('stand_left')
            if event.key == pygame.K_UP:
                self.update('stand_up')
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
            if event.key == pygame.K_DOWN:
                self.update('stand_down')

player = Player((50,60))


stars = [(350, 410), (940, 430), (590, 190)]

collected_stars = 0

heart_image = pygame.image.load('heart.png')
heart_image = pygame.transform.scale(heart_image, (40, 40))

clock = pygame.time.Clock()
enemy1 = Enemy(320, 490, 160, 100, 'enemy.png')
enemy2 = Enemy(960, 440, 160, 100, 'enemy.png')
door = Enemy(1860, 440, 120, 100, 'door.png')
level1 = True
level2 = False
game = True
pygame.mixer.music.play(-1)

# class Player(pygame.sprite.Sprite):
#     def __init__(self, position):
#         self.sheet = pygame.image.load('enemie1.png')
life = 3
zminna = 0
while game:
    if level1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        player.events(event)
        window.fill((0,0,0))
        window.blit(picture1,(0,0))
        
        window.blit(player.image, player.rect)
        window.blit(enemy1.image, (enemy1.rect.x, enemy1.rect.y))  
        window.blit(enemy2.image, (enemy2.rect.x, enemy2.rect.y))  
        window.blit(door.image, (door.rect.x, door.rect.y))  
        for w in walls:
            w.fill()
        zminna += 1
        if zminna == 40:
            enemy1.shoot()
            enemy2.shoot()
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
                    pygame.mixer.Sound.play(star_collect)
                    stars.remove(star)
                    collected_stars += 1
            
        if collected_stars > 2:
            door.rect.x, door.rect.y = 50, 100
            collected_stars = 0

        if player.rect.colliderect(door.rect):
            level1 = False
            level2 = True
            
            walls = [
                Wall(0, 0, 1200, 10),      
                Wall(0, 640, 1200, 10),    
                Wall(0, 0, 10, 650),       
                Wall(1190, 0, 10, 650),   
                Wall(100, 450, 10, 190),
                Wall(100, 210, 200, 10),  
                Wall(300, 10, 10, 110),    
                Wall(100, 320, 200, 10),   
                Wall(300, 220, 10, 220),   
                Wall(100, 440, 210, 10),  
                Wall(390, 440, 10, 190),   
                Wall(600, 10, 10, 300),   
                Wall(400, 10, 210, 10),    
                Wall(610, 200, 200, 10),   
                Wall(800, 10, 10, 200),   
                Wall(800, 300, 200, 10),   
                Wall(1000, 100, 10, 210),
                Wall(610, 400, 390, 10), 
                Wall(1000, 410, 10, 230), 
                Wall(800, 400, 10, 210),   
                Wall(610, 600, 200, 10), 
            ]


            player.rect.x, player.rect.y = 50, 50
            door.rect.x, door.rect.y = 1000,2000
            enemy1.rect.x, enemy1.rect.y = 1000,2000
            enemy2.rect.x, enemy2.rect.y = 1000,2000

            collected_stars = 0
            

        for star in stars:
            window.blit(star_image, star)

        for i in range(collected_stars):
            window.blit(star_image, (1050 + i * 40, 7))

        for i in range(life):
            window.blit(heart_image, (10 + i * (heart_image.get_width() + 5), 10))

   
    if level2:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        player.events(event)
        window.fill((0,0,0))
        window.blit(picture1,(0,0))
        
        window.blit(player.image, player.rect)
        window.blit(enemy1.image, (enemy1.rect.x, enemy1.rect.y))  
        window.blit(enemy2.image, (enemy2.rect.x, enemy2.rect.y))  
        window.blit(door.image, (door.rect.x, door.rect.y))  
        for w in walls:
            w.fill()
        for star in stars:
            window.blit(star_image, star)

        for i in range(collected_stars):
            window.blit(star_image, (1050 + i * 40, 7))

        for i in range(life):
            window.blit(heart_image, (10 + i * (heart_image.get_width() + 5), 10))
            


    

    clock.tick(30)
    pygame.display.update()