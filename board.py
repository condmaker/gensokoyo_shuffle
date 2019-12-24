import pygame
import pygame.freetype
import random
from gameboard import game_board

# Function that defines the display of the board dimension selection
def board_menu(song, click, back_click, musicStatus, res, unmute, mute, unmute_c, mute_c, mouse_motion):

    board_select_disp = pygame.display.set_mode(res)
    board_font = pygame.freetype.Font("fonts/BMSPA__.TTF", (15, 55))

    # Loads the background
    board_menu_bg = pygame.image.load("images/boardmenu_bg.png")
    
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
            
        # Loads the background
        board_select_disp.blit(board_menu_bg, (0, 0))

        # Gets the size of the text as an rectangle and uses it to center the text in the screen
        optionText = "Select your board!"
        selectText = board_font.get_rect(optionText)
        board_font.render_to(board_select_disp, (640 - (selectText[2] / 2) , 20), optionText, (129, 25, 55))

        # Renders the 'return' text
        returnText = "Return"
        returnTextSize = board_font.get_rect(returnText)
        board_font.render_to(board_select_disp, (1260 - (returnTextSize[2]) , 700 - (returnTextSize[3])), returnText, (129, 25, 55))

        # Draws the 4x3 rectangle option and text
        rect_4x3 = pygame.Rect(640 - 172.5, 120, 345, 50)
        pygame.draw.rect(board_select_disp, (145, 118, 144), rect_4x3, 0)
        text4x3 = "4x3"
        text4x3Size = board_font.get_rect(text4x3)
        board_font.render_to(board_select_disp, (640 - (text4x3Size[2] / 2), 120 + 25 - text4x3Size[3]/2), text4x3, (129, 25, 55))
        
        # Draws the 4x4 rectangle option
        rect_4x4 = pygame.Rect(640 - 172.5, 200, 345, 50)
        pygame.draw.rect(board_select_disp, (145, 118, 144), rect_4x4, 0)
        text4x4 = "4x4"
        text4x4Size = board_font.get_rect(text4x4)
        board_font.render_to(board_select_disp, (640 - (text4x4Size[2] / 2), 200 + 25 - text4x4Size[3]/2), text4x4, (129, 25, 55))

        # Draws the 5x4 rectangle option
        rect_5x4 = pygame.Rect(640 - 172.5, 280, 345, 50)
        pygame.draw.rect(board_select_disp, (145, 118, 144), rect_5x4, 0)
        text5x4 = "5x4"
        text5x4Size = board_font.get_rect(text5x4)
        board_font.render_to(board_select_disp, (640 - (text5x4Size[2] / 2), 280 + 25 - text5x4Size[3]/2), text5x4, (129, 25, 55))

        # Draws the 6x5 rectangle option
        rect_6x5 = pygame.Rect(640 - 172.5, 360, 345, 50)
        pygame.draw.rect(board_select_disp, (145, 118, 144), rect_6x5, 0)
        text6x5 = "6x5"
        text6x5Size = board_font.get_rect(text6x5)
        board_font.render_to(board_select_disp, (640 - (text6x5Size[2] / 2), 360 + 25 - text6x5Size[3]/2), text6x5, (129, 25, 55))

        # Draws the 6x6 rectangle option
        rect_6x6 = pygame.Rect(640 - 172.5, 440, 345, 50)
        pygame.draw.rect(board_select_disp, (145, 118, 144), rect_6x6, 0)
        text6x6 = "6x6"
        text6x6Size = board_font.get_rect(text6x6)
        board_font.render_to(board_select_disp, (640 - (text6x6Size[2] / 2), 440 + 25 - text6x6Size[3]/2), text6x6, (129, 25, 55))

        # Draws the images
        if (musicStatus):
            board_select_disp.blit(unmute, (20, 655))
        else:
            board_select_disp.blit(mute, (20, 655))

        # Updates the mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Verifies if player's mouse is inside the x axis of all buttons, and afterwards if it's inside the y position of the respective buttons
        if (mouse_x >= 467.5 and mouse_x <= 812.5):
            if (mouse_y >= 120 and mouse_y <= 170):
                pygame.draw.rect(board_select_disp, (200, 118, 144), rect_4x3, 0)
                board_font.render_to(board_select_disp, (640 - (text4x3Size[2] / 2), 120 + 25 - text4x3Size[3]/2), text4x3, (149, 25, 55))
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    click.play()
                    musicStatus = game_board(text4x3, res, mute, unmute, mute_c, unmute_c, mouse_motion, song, musicStatus, click, back_click)
            elif (mouse_y >= 200 and mouse_y <= 250):
                pygame.draw.rect(board_select_disp, (200, 118, 144), rect_4x4, 0)
                board_font.render_to(board_select_disp, (640 - (text4x4Size[2] / 2), 200 + 25 - text4x4Size[3]/2), text4x4, (149, 25, 55))
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    click.play()
                    musicStatus = game_board(text4x4, res, mute, unmute, mute_c, unmute_c, mouse_motion, song, musicStatus, click, back_click)
            elif (mouse_y >= 280 and mouse_y <= 330):
                pygame.draw.rect(board_select_disp, (200, 118, 144), rect_5x4, 0)
                board_font.render_to(board_select_disp, (640 - (text5x4Size[2] / 2), 280 + 25 - text5x4Size[3]/2), text5x4, (149, 25, 55))
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    click.play()
                    musicStatus = game_board(text5x4, res, mute, unmute, mute_c, unmute_c, mouse_motion, song, musicStatus, click, back_click)
            elif (mouse_y >= 360 and mouse_y <= 410):
                pygame.draw.rect(board_select_disp, (200, 118, 144), rect_6x5, 0)
                board_font.render_to(board_select_disp, (640 - (text6x5Size[2] / 2), 360 + 25 - text6x5Size[3]/2), text6x5, (149, 25, 55))
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    click.play()
                    musicStatus = game_board(text6x5, res, mute, unmute, mute_c, unmute_c, mouse_motion, song, musicStatus, click, back_click)
            elif (mouse_y >= 440 and mouse_y <= 490):
                pygame.draw.rect(board_select_disp, (200, 118, 144), rect_6x6, 0)
                board_font.render_to(board_select_disp, (640 - (text6x6Size[2] / 2), 440 + 25 - text6x6Size[3]/2), text6x6, (149, 25, 55))
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    click.play()
                    musicStatus = game_board(text6x6, res, mute, unmute, mute_c, unmute_c, mouse_motion, song, musicStatus, click, back_click)


        # Verifies if the player clicked the "Return" button
        if ((mouse_x >= 1182 and mouse_x <= 1260) and (mouse_y >= 657 and mouse_y <= 700)):
            board_font.render_to(board_select_disp, (1260 - (returnTextSize[2]) , 700 - (returnTextSize[3])), returnText, (149, 45, 75))
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                # Plays the 'click' SE
                back_click.play()

                # Delays the program
                pygame.time.delay(100)
                return musicStatus

        # Verifies if player's mouse is inside the mute button and mutes accordingly 
        if (mouse_motion):
            if (musicStatus == True):
                board_select_disp.blit(unmute_c, (20, 655))
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    song.pause()
                    musicStatus = False
                    pygame.time.delay(305)
            else: 
                board_select_disp.blit(mute_c, (20, 655))
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    song.unpause()
                    musicStatus = True
                    pygame.time.delay(305)

        pygame.display.flip()

#class game_card(text):