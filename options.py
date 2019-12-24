import pygame
import pygame.freetype
import random

def options_menu(song, click, back_click, musicStatus, res, mouse_x, mouse_y, unmute, mute, unmute_c, mute_c, mouse_motion):

    # Sets the display and the font that will be used
    options_menu_disp = pygame.display.set_mode(res)
    options_font = pygame.freetype.Font("fonts/BMSPA__.TTF", (15, 55))

    # Declaring the slider and line outside so it doesn't update
    vol_slider = pygame.Rect(640 - 20, 120 - 20, 40, 40)
    vol_line = pygame.Rect(467.5, 120, 345, 5)

    # Volume press variables
    vol_press = False
    vol_stat = False

    # The background image
    op_bg = pygame.image.load("images/options_bg.png")

    while(True):

        # Event observer
        for event in pygame.event.get():
            
            # Checks if the player quitted the game
            if (event.type == pygame.QUIT):
                exit()
            
            # Checks if the player muted the game with the 'm' key
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_m):
                    if (musicStatus == True):
                        song.pause()
                        musicStatus = False
                    else: 
                        song.unpause()
                        musicStatus = True
                elif (event.key == pygame.K_q):
                    exit()
            # Checks if the player muted the game by clicking on the icon, or if his mouse is hovering the volume slider
            if (event.type == pygame.MOUSEMOTION):
                if ((event.pos[0] >= 20 and event.pos[0] <= 70) and (event.pos[1] >= 655 and event.pos[1] <= 705)):
                    mouse_motion = True
                    vol_press = False
                    vol_stat = False
                elif ((event.pos[0] >= vol_line[0] and event.pos[0] <= vol_line[0] + 345) and (event.pos[1] >= vol_line[1] and event.pos[1] <= vol_line[1] + 40)):
                    vol_press = True
                    vol_stat = False
                else:
                    mouse_motion = False
                    vol_press = False
                    vol_stat = False

            # If the player's mouse is hovering the volume slider and he clicks on it, it activates an variable that tells the program he clicked on it
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (vol_press):
                    vol_stat = True
                else: 
                    vol_stat = False
                    

        options_menu_disp.fill((0,10,0))

        # Renders the background
        options_menu_disp.blit(op_bg, (0, 0))
        
        # Renders the "Volume" text
        volText = "Volume"
        volTextSize = options_font.get_rect(volText)
        options_font.render_to(options_menu_disp, (640 - (volTextSize[2] / 2) , 20), volText, (129, 25, 55))

        # Renders the 'return' text
        returnText = "Return"
        returnTextSize = options_font.get_rect(returnText)
        options_font.render_to(options_menu_disp, (1260 - (returnTextSize[2]) , 700 - (returnTextSize[3])), returnText, (129, 25, 55))

        # Renders and draws the volume line and slider
        pygame.draw.rect(options_menu_disp, (232, 150, 167), vol_line, 0)
        pygame.draw.rect(options_menu_disp, (129, 25, 55), vol_slider, 0)

        # Draws the images
        if (musicStatus):
            options_menu_disp.blit(unmute, (20, 655))
        else:
            options_menu_disp.blit(mute, (20, 655))

        # Gets the mouse position to determine clicks
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Verifies if the player is in the volume
        if (vol_stat):
            vol_slider[0] = mouse_x - 20  # 467.5 - 1%    812.5 - 100%
            lesongvol = (vol_slider[0] - 467.5) * 0.5 / 172.5 # <-- NEEDS TO FIX!
            song.set_volume(lesongvol)

        # Verifies if the player clicked the "Return" button
        if ((mouse_x >= 1182 and mouse_x <= 1260) and (mouse_y >= 657 and mouse_y <= 700)):
            options_font.render_to(options_menu_disp, (1260 - (returnTextSize[2]) , 700 - (returnTextSize[3])), returnText, (149, 45, 75))
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                # Plays the 'click' SE
                back_click.play()

                # Delays the program
                pygame.time.delay(100)
                return musicStatus

        # Verifies if player's mouse is inside the mute button and mutes accordingly 
        if (mouse_motion):
            if (musicStatus == True):
                options_menu_disp.blit(unmute_c, (20, 655))
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    song.pause()
                    musicStatus = False
                    pygame.time.delay(305)
            else: 
                options_menu_disp.blit(mute_c, (20, 655))
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    song.unpause()
                    musicStatus = True
                    pygame.time.delay(305)
        
        pygame.display.flip()
