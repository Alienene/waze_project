import pygame

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
        self.sheet.set_clip(pygame.Rect(0,0,48,64))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0 # рамка
        self.down = {
    0: (0, 0, 48, 64), 
    1: (48, 0, 48, 64), 
    2: (96, 0, 48, 64),
    3: (144, 0, 48, 64)
}
        self.left = {
    0: (0, 64, 48, 64), 
    1: (48, 64, 48, 64), 
    2: (96, 64, 48, 64),
    3: (144, 64, 48, 64)
}
        self.right = {
    0: (0, 128, 48, 64), 
    1: (48, 128, 48, 64), 
    2: (96, 128, 48, 64),
    3: (144, 128, 48, 64)
}
        self.up = {
    0: (0, 192, 48, 64), 
    1: (48, 192, 48, 64), 
    2: (96, 192, 48, 64),
    3: (144, 192, 48, 64)
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
            self.rect.y += 5
            for w in walls:
                if player.rect.colliderect(w.rect):
                    player.rect.bottom = w.rect.top
        if direction == "left":
            self.clip(self.left)
            self.rect.x -= 5  
            for w in walls:
                if player.rect.colliderect(w.rect):
                    player.rect.left = w.rect.right
        if direction == "right":
            self.clip(self.right)
            self.rect.x += 5 
            for w in walls:
                if player.rect.colliderect(w.rect):
                    player.rect.right = w.rect.left
        if direction == "up":
            self.clip(self.up)
            self.rect.y -= 5 
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