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
    

    def __init__(self, x, y, attack_range, bullets):
        self.x = x
        self.y = y
        self.attack_range = attack_range
        self.bullets = bullets 

    def distance_to_player(self, player):
        return ((self.x - player.x) ** 2 + (self.y - player.y) ** 2) ** 0.5

    def update(self, player):
        if self.distance_to_player(player) < self.attack_range:
            self.attack(player)

    def attack(self, player):
        bullet = Bullet(self.x, self.y, player.x, player.y)
        self.bullets.append(bullet)


class Bullet:
    def __init__(self, x, y, target_x, target_y):
        self.x = x
        self.y = y
        self.target_x = target_x
        self.target_y = target_y
        self.speed = 5  # Скорость пули

    def move(self):
        direction_x = self.target_x - self.x
        direction_y = self.target_y - self.y
        distance = (direction_x ** 2 + direction_y ** 2) ** 0.5


        direction_x /= distance
        direction_y /= distance

        self.x += direction_x * self.speed
        self.y += direction_y * self.speed

    def check_collision_with_walls(self, walls):
        for wall in walls:
            if wall.collides_with(self.x, self.y):
                return True
        return False
    
    
