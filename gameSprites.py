import pygame as pg

class PlayerSprite(pg.sprite.Sprite):
    """player controlled charecter"""
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
    
    def update(self):
        pass

class Obsticale(pg.sprite.Sprite):
    """obsticale needed to be dodged"""
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

    def update(self):
        pass
