import pygame  as pg
import pygame_gui as gui

from gameSprites import *

def main():
    """This is the Game's main function"""
    pg.init()
    pg.display.set_caption('Game')
    window_surface = pg.display.set_mode((800, 600))
    background = pg.Surface((800, 600))
    background.fill(pg.Color('#000000'))
    manager = gui.UIManager((800, 600))
    clock = pg.time.Clock()

    # example button:
    hello_button = gui.elements.UIButton(relative_rect=pg.Rect((350, 275), (100, 50)),
                                             text='Say Hello',
                                             manager=manager)

    
    platform  = Planform()
    player = PlayerSprite(platform.rect)

    generalSprites = (pg.sprite.Group(platform)) #sprites that are for show
    obsticale = Obsticale(platform.rect)
    obsticales = pg.sprite.Group(obsticale)
    is_running = True

    while is_running:
        time_delta = clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_running = False
            if event.type == pg.USEREVENT:
                if event.user_type == gui.UI_BUTTON_PRESSED:
                    if event.ui_element == hello_button:
                        print('Hello World!')
            manager.process_events(event)

        #updates
        manager.update(time_delta)
        player.update()
        obsticales.update()

        #ToDo: preform a collision cheak of obsticale with the player


        #draw
        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)
        generalSprites.draw(window_surface)
        obsticales.draw(window_surface)
        player.draw(window_surface)
        
        pg.display.update()
        



if __name__ == '__main__':
    main()
