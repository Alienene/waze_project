import pygame
class Enemy(): # клас для створення шаблону персонажа
    def __init__(self,x,y,width,height,image):
        self.original_image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.original_image, (width, height))  # Зміна розміру зображення
        self.rect = self.image.get_rect() # "межі" персонажа
        self.rect.x = x # координати по ширині
        self.rect.y = y # координати по висоті
        self.width = width # ширина
        self.height = height # висота
    
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.centery) # створення пулі
        bullets.append(bullet) # додавання пулі до списку пуль
    
    # def __init__(self, x, y, attack_range, bullets):
    #     self.x = x
    #     self.y = y
    #     self.attack_range = attack_range
    #     self.bullets = bullets 

    # def distance_to_player(self, player):
    #     return ((self.x - player.x) ** 2 + (self.y - player.y) ** 2) ** 0.5

    # def update(self, player):
    #     if self.distance_to_player(player) < self.attack_range:
    #         self.attack(player)

    # def attack(self, player):
    #     bullet = Bullet(self.x, self.y, player.x, player.y)
    #     self.bullets.append(bullet)


bullets = [] # створення списку пуль
class Bullet():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 5, 5) # 5,5 - розміри пулі

    def move(self): # функція для створення руху пулі
        self.rect.x -= 10 # 10 - швидкість пулі
    
    
