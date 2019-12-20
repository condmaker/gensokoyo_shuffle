import pygame
import pygame.freetype
import random

def options_menu(song, click, back_click, musicStatus, res, mouse_x, mouse_y, unmute, mute, unmute_c, mute_c, mouse_motion):

    # Sets the display and the font that will be used
    options_menu_disp = pygame.display.set_mode(res)
    options_font = pygame.freetype.Font("BMSPA__.TTF", (15, 55))

    while(True):

        # Observes if the player muted the song (with 'M' or by clicking the image) or quitted the game
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_m):
                    if (musicStatus == True):
                        song.pause()
                        musicStatus = False
                    else: 
                        song.unpause()
                        musicStatus = True
            if (event.type == pygame.MOUSEMOTION):
                if ((event.pos[0] >= 20 and event.pos[0] <= 70) and (event.pos[1] >= 655 and event.pos[1] <= 705)):
                    mouse_motion = True
                else:
                    mouse_motion = False

        options_menu_disp.fill((0,10,0))

        # Renders the "Volume" text
        volText = "Volume"
        volTextSize = options_font.get_rect(volText)
        options_font.render_to(options_menu_disp, (640 - (volTextSize[2] / 2) , 20), volText, (129, 25, 55))

        # Renders the 'return' text
        returnText = "Return"
        returnTextSize = options_font.get_rect(returnText)
        options_font.render_to(options_menu_disp, (1260 - (returnTextSize[2]) , 700 - (returnTextSize[3])), returnText, (129, 25, 55))

        # Draws the images
        if (musicStatus):
            options_menu_disp.blit(unmute, (20, 655))
        else:
            options_menu_disp.blit(mute, (20, 655))

        # Gets the mouse position to determine clicks
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Verifies if the player clicked the "Return" button
        if ((mouse_x >= 1182 and mouse_x <= 1260) and (mouse_y >= 657 and mouse_y <= 700)):
            options_font.render_to(options_menu_disp, (1260 - (returnTextSize[2]) , 700 - (returnTextSize[3])), returnText, (149, 45, 75))
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                # Plays the 'click' SE
                back_click.play()

                # Delays the program
                pygame.time.delay(100)
                return

        # Verifies if player's mouse is inside the mute button and mutes accordingly 
        if (mouse_motion):
            if (musicStatus == True):
                options_menu_disp.blit(unmute_c, (20, 655))
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    song.pause()
                    musicStatus = False
                    pygame.time.delay(5)
            else: 
                options_menu_disp.blit(mute_c, (20, 655))
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    song.unpause()
                    musicStatus = True
                    pygame.time.delay(5)
        
        pygame.display.flip()