import pygame as pg
from pygame.draw import rect
from pygame.locals import *

# ToDo: get the actual screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WIDTH = 64
HEIGHT = 64

class PlayerSprite(pg.sprite.Sprite):
    """player controlled charecter, provide a rect for movment"""
    def __init__(self, platform_rect):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([WIDTH, HEIGHT])
        self.image.fill(pg.Color(50, 168, 82))
        self.rect = self.image.get_rect(topleft = (SCREEN_WIDTH/4,SCREEN_HEIGHT-HEIGHT-100))
        self.platform_rect = platform_rect.inflate(-platform_rect.width/5, -HEIGHT) #makes the rect smaller so it fits the image
        self.rect.centerx = self.platform_rect.centerx

    def update(self):
        """moves the player"""
        pressed_keys = pg.key.get_pressed()
        if self.rect.left > self.platform_rect.left:   #1/4 of the screen is for the left limit
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right <self.platform_rect.right:  #3/4 of the screen is for the left limit 
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Obsticale(pg.sprite.Sprite):
    """obsticale needed to be dodged"""
    def __init__(self, platform_rect):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([32,32])
        self.image.fill(pg.Color(22, 130, 111))
        self.platform_rect = platform_rect
        self.rect = self.image.get_rect(topleft = (self.platform_rect.centerx,self.platform_rect.height//4))

    def update(self):
        """increase the size of self rect, image, each call.
        on max size Obsticale is killed"""
        self.rect.move_ip(0, 3)
        self.image = pg.transform.scale(self.image,(self.rect.width + 1,self.rect.height +1))   #too fast
        self.rect = self.image.get_rect(topleft= self.rect.topleft)
        if(not self.platform_rect.contains(self.rect)):
            print("killed")
            self.kill()
        

class Planform(pg.sprite.Sprite):
    """The platform player charecter is running on"""
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        # self.image = pg.Surface([SCREEN_WIDTH/2,SCREEN_HEIGHT])
        # self.image.fill(pg.Color(100, 130, 200))
        self.image = pg.transform.scale(pg.image.load(r"resources\models\platform.png"),(SCREEN_WIDTH//2,SCREEN_HEIGHT)).convert_alpha()
        self.rect = self.image.get_rect(topleft = (SCREEN_WIDTH/4,0))

    def update(self):
        """cycle animations of the platform"""
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)


