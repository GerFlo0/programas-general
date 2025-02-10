import pygame, const

class Txt():
    def __init__(self, type=str) -> None:
        self.type = type
        self.size = const.SIZES[self.type]
        self.img = pygame.image.load(const.TEXTURES[self.type]).convert_alpha()

class Sprite(Txt):
    def __init__(self, x=int, y=int, type=str) -> None:
        super().__init__(type)
        self.x = x
        self.y = y
    
    def draw(self, img, screen = pygame.surface.Surface):
        screen.blit(img, (self.x, self.y))

class General(Sprite):
    def __init__(self, x=int, y=int, type=str, live=bool) -> None:
        super().__init__(x, y, type)
        self.vel = const.VELS[f"{self.type}_vel"]
        self.live = live
        self.center = (0,0)
    
    def move_to(self, x=int, y=int):
        self.x = x
        self.y = y
        self.center = (self.x+int(self.size[0]/2),self.y+int(self.size[1]/2))

class Meteor(General):
    def __init__(self, x=int, y=int, type=str, live=bool) -> None:
        super().__init__(x, y, type, live)
        self.img_hurt = [pygame.image.load(const.TEXTURES[f"{self.type}_{i+1}"]).convert_alpha() for i in range(3)]
        self.dying = -1
        self.dying_counter = 0

class Ship(General):
    def __init__(self, x=int, y=int, type=str) -> None:
        super().__init__(x, y, type)
        
        self.img_hurt = pygame.image.load(const.TEXTURES[f"{type}_hurt"]).convert_alpha()
        
        self.img_damaged = [pygame.image.load(const.TEXTURES[f"{type}_{i+1}"]).convert_alpha() for i in range(3)]
        
        self.cannons = [(0,0) for i in range(const.CANNONS[self.type])]
        self.bull_cad = const.VELS[f"{self.type}_bullet_cad"]
        self.hearts = const.HEARTS[self.type]
    
    def update_cannons_pos(self):
        if self.type == "player":
            self.cannons[0]=(self.x, self.y+20)
            self.cannons[1]=(self.x+30, self.y+20)
            
        elif self.type == "boss":
            self.cannons[0]=(self.x, self.y+self.size[1]-50)
            self.cannons[1]=(self.x+70, self.y+self.size[1]-30)
            self.cannons[2]=(self.x+140, self.y+self.size[1]-50)
    
    def shoot(self, bullets_list=list, cannon=int):
        for bullet in bullets_list:
            if not bullet.live:
                bullet.live = True
                bullet.move_to(self.cannons[cannon][0], self.cannons[cannon][1])
                break

class Player_ship(Ship):
    def __init__(self, x=int, y=int, type=str) -> None:
        super().__init__(x, y, type)
    
    def move(self, keys=list):
        if keys[pygame.K_w] and self.y > 0:
            self.move_to(self.x, self.y-self.vel)
        
        if keys[pygame.K_s] and self.y < const.SIZES["screen"][1]-self.size[1]:
            self.move_to(self.x, self.y+self.vel)
        
        if keys[pygame.K_a] and self.x > 0:
            self.move_to(self.x-self.vel, self.y)
        
        if keys[pygame.K_d] and self.x < const.SIZES["screen"][0]-self.size[0]:
            self.move_to(self.x+self.vel, self.y)
        
        self.update_cannons_pos()

class Boss_ship(Ship):
    def __init__(self, x=int, y=int, type=str) -> None:
        super().__init__(x, y, type)
    
    def move(self, x=int, y=int):
        self.move_to(x, y)
        self.update_cannons_pos()