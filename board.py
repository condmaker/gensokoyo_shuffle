import pygame
import pygame.freetype
import random

# Function that defines the display of the board dimension selection
def board_menu(song, click, back_click, musicStatus, res, unmute, mute, unmute_c, mute_c, mouse_motion):

    board_select_disp = pygame.display.set_mode(res)
    board_font = pygame.freetype.Font("BMSPA__.TTF", (15, 55))
    

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

        # Fills the screen 
        board_select_disp.fill((0,10,0))
            
        # Gets the size of the text as an rectangle and uses it to center the text in the screen
        optionText = "Select your board!"
        selectText = board_font.get_rect(optionText)
        board_font.render_to(board_select_disp, (640 - (selectText[2] / 2) , 20), optionText, (129, 25, 55))

        # Renders the 'return' text
        returnText = "Return"
        returnTextSize = board_font.get_rect(returnText)
        board_font.render_to(board_select_disp, (1260 - (returnTextSize[2]) , 700 - (returnTextSize[3])), returnText, (129, 25, 55))

        # Updates the mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Draws the 4x3 rectangle option
        rect_4x3 = pygame.Rect(640 - 172.5, 120, 345, 50)
        pygame.draw.rect(board_select_disp, (145, 118, 144), rect_4x3, 0)
        
        # Draws the 4x4 rectangle option
        rect_4x4 = pygame.Rect(640 - 172.5, 200, 345, 50)
        pygame.draw.rect(board_select_disp, (145, 118, 144), rect_4x4, 0)

        # Draws the 5x4 rectangle option
        rect_5x4 = pygame.Rect(640 - 172.5, 280, 345, 50)
        pygame.draw.rect(board_select_disp, (145, 118, 144), rect_5x4, 0)

        # Draws the 6x5 rectangle option
        rect_6x5 = pygame.Rect(640 - 172.5, 360, 345, 50)
        pygame.draw.rect(board_select_disp, (145, 118, 144), rect_6x5, 0)

        # Draws the 6x6 rectangle option
        rect_6x6 = pygame.Rect(640 - 172.5, 440, 345, 50)
        pygame.draw.rect(board_select_disp, (145, 118, 144), rect_6x6, 0)

        # Draws the images
        if (musicStatus):
            board_select_disp.blit(unmute, (20, 655))
        else:
            board_select_disp.blit(mute, (20, 655))

        # Verifies if the player clicked the "Return" button
        if ((mouse_x >= 1182 and mouse_x <= 1260) and (mouse_y >= 657 and mouse_y <= 700)):
            board_font.render_to(board_select_disp, (1260 - (returnTextSize[2]) , 700 - (returnTextSize[3])), returnText, (149, 45, 75))
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                # Plays the 'click' SE
                back_click.play()

                # Delays the program
                pygame.time.delay(100)
                return

        # Verifies if player's mouse is inside the mute button and mutes accordingly 
        if (mouse_motion):
            if (musicStatus == True):
                board_select_disp.blit(unmute_c, (20, 655))
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    song.pause()
                    musicStatus = False
                    pygame.time.delay(5)
            else: 
                board_select_disp.blit(mute_c, (20, 655))
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    song.unpause()
                    musicStatus = True
                    pygame.time.delay(5)

        pygame.display.flip()

