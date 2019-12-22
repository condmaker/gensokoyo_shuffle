import pygame
import pygame.freetype
import random

def game_board(text, res, mute, unmute, mute_c, unmute_c, mouse_motion, song, musicStatus, click, back_click):

    game_board_disp = pygame.display.set_mode(res)
    game_board_font = pygame.freetype.Font("fonts/BMSPA__.TTF", (15, 55))

    # Loads the background
    game_bg = pygame.image.load("images/game_bg.png")

    # Loads the cards
    c1 = pygame.image.load("images/spellcard_black.png")
    c2 = pygame.image.load("images/spellcard_blue.png")
    c3 = pygame.image.load("images/spellcard_green.png")
    c4 = pygame.image.load("images/spellcard_grey.png")
    c5 = pygame.image.load("images/spellcard_orange.png")
    c6 = pygame.image.load("images/spellcard_pink.png")
    c7 = pygame.image.load("images/spellcard_purple.png")
    c8 = pygame.image.load("images/spellcard_red.png")
    c9 = pygame.image.load("images/spellcard_yellow.png")
    c10 = pygame.image.load("images/yingyangball.png")
    c11 = pygame.image.load("images/yingyangballblue.png")
    c12 = pygame.image.load("images/yingyangballgreen.png")
    c13 = pygame.image.load("images/yingyangballgrey.png")
    c14 = pygame.image.load("images/yingyangballorange.png")
    c15 = pygame.image.load("images/yingyangballpink.png")
    c16 = pygame.image.load("images/yingyangballpurple.png")
    c17 = pygame.image.load("images/yingyangballred.png")
    c18 = pygame.image.load("images/yingyangballyellow.png")

    # Defines number of cards and number of pairs based on argument given 'text'
    dictionary = {
        "4x3": (12, 6, (4, 3)),
        "4x4": (16, 8, (4, 4)),
        "5x4": (20, 10, (5, 4)),
        "6x5": (30, 15, (6, 5)),
        "6x6": (36, 18, (6, 6))
    }
    for index in dictionary:
        if (text == index):
            board_type = dictionary[index]

    # Defines the cards for the current session
    cards_fulldeck = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18]
    cards_ordered = []
    cards = []
    for index in range(0, board_type[1]):
        # Chosses a random card from cards_fulldeck, and appends it two times in the list (so it has a pair)
        chosen_card = random.choice(cards_fulldeck)
        cards_fulldeck.remove(chosen_card)
        cards_ordered.append(chosen_card)
        cards_ordered.append(chosen_card)
    
    # Puts the cards out of order
    for index in range(0, board_type[0]):
        chosen_card_final = random.choice(cards_ordered)
        cards_ordered.remove(chosen_card_final)
        cards.append(chosen_card_final)

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
                        print(str(len(cards)))
                    else: 
                        song.unpause()
                        musicStatus = True
                elif (event.key == pygame.K_q):
                    exit()
            if (event.type == pygame.MOUSEMOTION):
                if ((event.pos[0] >= 20 and event.pos[0] <= 70) and (event.pos[1] >= 655 and event.pos[1] <= 705)):
                    mouse_motion = True
                else:
                    mouse_motion = False
        
        # Fills the screen 
        game_board_disp.fill((0,10,0))

        # Renders the background
        game_board_disp.blit(game_bg, (0,0))

        # Renders the 'return' text
        returnText = "Return"
        returnTextSize = game_board_font.get_rect(returnText)
        game_board_font.render_to(game_board_disp, (1260 - (returnTextSize[2]) , 700 - (returnTextSize[3])), returnText, (129, 25, 55))

        # Renders the 'points' text
        pointsText = "Points:"
        pointsTextSize = game_board_font.get_rect(pointsText)
        game_board_font.render_to(game_board_disp, (25, 25), pointsText, (102, 30, 47), None, pygame.freetype.STYLE_OBLIQUE)
        game_board_font.render_to(game_board_disp, (20, 20), pointsText, (232, 150, 167), None, pygame.freetype.STYLE_OBLIQUE)

        # Renders and defines the total space of the card space
        card_space = pygame.Rect(1280/4, 20, 640, 680)

        # Draws the horizontal cards in the specific board
        # 0 row
        card0_1 = pygame.Rect(1280/4, 20, 640/board_type[2][0], 680/board_type[2][1])
        pygame.draw.rect(game_board_disp, (129, 25, 55), card0_1, 1)

        card0_2 = pygame.Rect(1280/4 + 640/board_type[2][0], 20, 640/board_type[2][0], 680/board_type[2][1])
        pygame.draw.rect(game_board_disp, (129, 25, 55), card0_2, 1)

        card0_3 = pygame.Rect(1280/4 + 2*(640/board_type[2][0]), 20, 640/board_type[2][0], 680/board_type[2][1])
        pygame.draw.rect(game_board_disp, (129, 25, 55), card0_3, 1)

        card0_4 = pygame.Rect(1280/4 + 3*(640/board_type[2][0]), 20, 640/board_type[2][0], 680/board_type[2][1])
        pygame.draw.rect(game_board_disp, (129, 25, 55), card0_4, 1)

        if(board_type[2][0] == 5 or board_type[2][0] == 6):
            card0_5 = pygame.Rect(1280/4 + 4*(640/board_type[2][0]), 20, 640/board_type[2][0], 680/board_type[2][1])
            pygame.draw.rect(game_board_disp, (129, 25, 55), card0_5, 1)
            if(board_type[2][0] == 6):
                card0_6 = pygame.Rect(1280/4 + 5*(640/board_type[2][0]), 20, 640/board_type[2][0], 680/board_type[2][1])
                pygame.draw.rect(game_board_disp, (129, 25, 55), card0_6, 1)
            
        # 1 row
        card1_1 = pygame.Rect(1280/4, 20 + 680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
        pygame.draw.rect(game_board_disp, (129, 25, 55), card1_1, 1)
        
        card1_2 = pygame.Rect(1280/4 + 640/board_type[2][0], 20 + 680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
        pygame.draw.rect(game_board_disp, (129, 25, 55), card1_2, 1)

        card1_3 = pygame.Rect(1280/4 + 2*(640/board_type[2][0]), 20 + 680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
        pygame.draw.rect(game_board_disp, (129, 25, 55), card1_3, 1)

        card1_4 = pygame.Rect(1280/4 + 3*(640/board_type[2][0]), 20 + 680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
        pygame.draw.rect(game_board_disp, (129, 25, 55), card1_4, 1)

        if(board_type[2][0] == 5 or board_type[2][0] == 6):
            card1_5 = pygame.Rect(1280/4 + 4*(640/board_type[2][0]), 20 + 680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
            pygame.draw.rect(game_board_disp, (129, 25, 55), card1_5, 1)
            if(board_type[2][0] == 6):
                card1_6 = pygame.Rect(1280/4 + 5*(640/board_type[2][0]), 20 + 680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
                pygame.draw.rect(game_board_disp, (129, 25, 55), card1_6, 1)

        # 2 row
        card2_1 = pygame.Rect(1280/4, 20 + 2*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
        pygame.draw.rect(game_board_disp, (129, 25, 55), card2_1, 1)

        card2_2 = pygame.Rect(1280/4 + 640/board_type[2][0], 20 + 2*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
        pygame.draw.rect(game_board_disp, (129, 25, 55), card2_2, 1)

        card2_3 = pygame.Rect(1280/4 + 2*(640/board_type[2][0]), 20 + 2*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
        pygame.draw.rect(game_board_disp, (129, 25, 55), card2_3, 1)

        card2_4 = pygame.Rect(1280/4 + 3*(640/board_type[2][0]), 20 + 2*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
        pygame.draw.rect(game_board_disp, (129, 25, 55), card2_4, 1)

        if(board_type[2][0] == 5 or board_type[2][0] == 6):
            card2_5 = pygame.Rect(1280/4 + 4*(640/board_type[2][0]), 20 + 2*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
            pygame.draw.rect(game_board_disp, (129, 25, 55), card2_5, 1)
            if(board_type[2][0] == 6):
                card2_6 = pygame.Rect(1280/4 + 5*(640/board_type[2][0]), 20 + 2*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
                pygame.draw.rect(game_board_disp, (129, 25, 55), card2_6, 1)

        # 3 row
        if(board_type[2][1] == 4 or board_type[2][1] == 5 or board_type[2][1] == 6):
            card3_1 = pygame.Rect(1280/4, 20 + 3*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
            pygame.draw.rect(game_board_disp, (129, 25, 55), card3_1, 1)

            card3_2 = pygame.Rect(1280/4 + 640/board_type[2][0], 20 + 3*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
            pygame.draw.rect(game_board_disp, (129, 25, 55), card3_2, 1)

            card3_3 = pygame.Rect(1280/4 + 2*(640/board_type[2][0]), 20 + 3*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
            pygame.draw.rect(game_board_disp, (129, 25, 55), card3_3, 1)

            card3_4 = pygame.Rect(1280/4 + 3*(640/board_type[2][0]), 20 + 3*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
            pygame.draw.rect(game_board_disp, (129, 25, 55), card3_4, 1)

            if(board_type[2][0] == 5 or board_type[2][0] == 6):
                card3_5 = pygame.Rect(1280/4 + 4*(640/board_type[2][0]), 20 + 3*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
                pygame.draw.rect(game_board_disp, (129, 25, 55), card3_5, 1)
                if(board_type[2][0] == 6):
                    card3_6 = pygame.Rect(1280/4 + 5*(640/board_type[2][0]), 20 + 3*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
                    pygame.draw.rect(game_board_disp, (129, 25, 55), card3_6, 1)

            # 4 row    
            if(board_type[2][1] == 5 or board_type[2][1] == 6):
                card4_1 = pygame.Rect(1280/4, 20 + 4*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
                pygame.draw.rect(game_board_disp, (129, 25, 55), card4_1, 1)

                card4_2 = pygame.Rect(1280/4 + 640/board_type[2][0], 20 + 4*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
                pygame.draw.rect(game_board_disp, (129, 25, 55), card4_2, 1)

                card4_3 = pygame.Rect(1280/4 + 2*(640/board_type[2][0]), 20 + 4*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
                pygame.draw.rect(game_board_disp, (129, 25, 55), card4_3, 1)

                card4_4 = pygame.Rect(1280/4 + 3*(640/board_type[2][0]), 20 + 4*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
                pygame.draw.rect(game_board_disp, (129, 25, 55), card4_4, 1)

                if(board_type[2][0] == 5 or board_type[2][0] == 6):
                    card4_5 = pygame.Rect(1280/4 + 4*(640/board_type[2][0]), 20 + 4*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
                    pygame.draw.rect(game_board_disp, (129, 25, 55), card4_5, 1)
                    if (board_type[2][0] == 6):
                        card4_6 = pygame.Rect(1280/4 + 5*(640/board_type[2][0]), 20 + 4*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
                        pygame.draw.rect(game_board_disp, (129, 25, 55), card4_6, 1)

                # 5 row
                if(board_type[2][1] == 6):
                    card5_1 = pygame.Rect(1280/4, 20 + 5*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
                    pygame.draw.rect(game_board_disp, (129, 25, 55), card5_1, 1)

                    card5_2 = pygame.Rect(1280/4 + 640/board_type[2][0], 20 + 5*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
                    pygame.draw.rect(game_board_disp, (129, 25, 55), card5_2, 1)

                    card5_3 = pygame.Rect(1280/4 + 2*(640/board_type[2][0]), 20 + 5*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
                    pygame.draw.rect(game_board_disp, (129, 25, 55), card5_3, 1)

                    card5_4 = pygame.Rect(1280/4 + 3*(640/board_type[2][0]), 20 + 5*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
                    pygame.draw.rect(game_board_disp, (129, 25, 55), card5_4, 1)

                    if(board_type[2][0] == 5 or board_type[2][0] == 6):
                        card5_5 = pygame.Rect(1280/4 + 4*(640/board_type[2][0]), 20 + 5*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
                        pygame.draw.rect(game_board_disp, (129, 25, 55), card5_5, 1)
                        if(board_type[2][0] == 6):
                            card5_6 = pygame.Rect(1280/4 + 5*(640/board_type[2][0]), 20 + 5*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])
                            pygame.draw.rect(game_board_disp, (129, 25, 55), card5_6, 1)
        
        # Draws the images
        if (musicStatus):
            game_board_disp.blit(unmute, (20, 655))
        else:
            game_board_disp.blit(mute, (20, 655))

        # Updates the mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Verifies if the player clicked the "Return" button
        if ((mouse_x >= 1182 and mouse_x <= 1260) and (mouse_y >= 657 and mouse_y <= 700)):
            game_board_font.render_to(game_board_disp, (1260 - (returnTextSize[2]) , 700 - (returnTextSize[3])), returnText, (149, 45, 75))
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                # Plays the 'click' SE
                back_click.play()

                # Delays the program
                pygame.time.delay(100)
                return
        
        # Verifies if player's mouse is inside the mute button and mutes accordingly 
        if (mouse_motion):
            if (musicStatus == True):
                game_board_disp.blit(unmute_c, (20, 655))
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    song.pause()
                    musicStatus = False
                    pygame.time.delay(305)
            else: 
                game_board_disp.blit(mute_c, (20, 655))
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    song.unpause()
                    musicStatus = True
                    pygame.time.delay(305)
        
        # Verifies if player's mouse is inside one of the cards

        # 0 row
        if ((mouse_x >= card0_1[0] and mouse_x <= card0_1[0] + card0_1[2]) and (mouse_y >= card0_1[1] and mouse_y <= card0_1[1] + card0_1[3])):
            pygame.draw.rect(game_board_disp, (200, 118, 144), card0_1, 0)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                game_board_disp.blit(cards[0], (40,40))

        if ((mouse_x >= card0_2[0] and mouse_x <= card0_2[0] + card0_2[2]) and (mouse_y >= card0_2[1] and mouse_y <= card0_2[1] + card0_2[3])):
            pygame.draw.rect(game_board_disp, (200, 118, 144), card0_2, 0)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                game_board_disp.blit(cards[1], (40,40))

        if ((mouse_x >= card0_3[0] and mouse_x <= card0_3[0] + card0_3[2]) and (mouse_y >= card0_3[1] and mouse_y <= card0_3[1] + card0_3[3])):
            pygame.draw.rect(game_board_disp, (200, 118, 144), card0_3, 0)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                game_board_disp.blit(cards[2], (40,40))

        if ((mouse_x >= card0_4[0] and mouse_x <= card0_4[0] + card0_4[2]) and (mouse_y >= card0_4[1] and mouse_y <= card0_4[1] + card0_4[3])):
            pygame.draw.rect(game_board_disp, (200, 118, 144), card0_4, 0)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                game_board_disp.blit(cards[3], (40,40))
        
        if (board_type[2][0] == 5 or board_type[2][0] == 6):
            if ((mouse_x >= card0_5[0] and mouse_x <= card0_5[0] + card0_5[2]) and (mouse_y >= card0_5[1] and mouse_y <= card0_5[1] + card0_5[3])):
                pygame.draw.rect(game_board_disp, (200, 118, 144), card0_5, 0)
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    game_board_disp.blit(cards[20], (40,40))
            if (board_type[2][0] == 6):
                if ((mouse_x >= card0_6[0] and mouse_x <= card0_6[0] + card0_6[2]) and (mouse_y >= card0_6[1] and mouse_y <= card0_6[1] + card0_6[3])):
                    pygame.draw.rect(game_board_disp, (200, 118, 144), card0_6, 0)
                    if (pygame.mouse.get_pressed() == (1, 0, 0)):
                        game_board_disp.blit(cards[25], (40,40))

        # 1 row
        if ((mouse_x >= card1_1[0] and mouse_x <= card1_1[0] + card1_1[2]) and (mouse_y >= card1_1[1] and mouse_y <= card1_1[1] + card1_1[3])):
            pygame.draw.rect(game_board_disp, (200, 118, 144), card1_1, 0)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                game_board_disp.blit(cards[4], (40,40))

        if ((mouse_x >= card1_2[0] and mouse_x <= card1_2[0] + card1_2[2]) and (mouse_y >= card1_2[1] and mouse_y <= card1_2[1] + card1_2[3])):
            pygame.draw.rect(game_board_disp, (200, 118, 144), card1_2, 0)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                game_board_disp.blit(cards[5], (40,40))

        if ((mouse_x >= card1_3[0] and mouse_x <= card1_3[0] + card1_3[2]) and (mouse_y >= card1_3[1] and mouse_y <= card1_3[1] + card1_3[3])):
            pygame.draw.rect(game_board_disp, (200, 118, 144), card1_3, 0)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                game_board_disp.blit(cards[6], (40,40))
        
        if ((mouse_x >= card1_4[0] and mouse_x <= card1_4[0] + card1_4[2]) and (mouse_y >= card1_4[1] and mouse_y <= card1_4[1] + card1_4[3])):
            pygame.draw.rect(game_board_disp, (200, 118, 144), card1_4, 0)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                game_board_disp.blit(cards[7], (40,40))

        if (board_type[2][0] == 5 or board_type[2][0] == 6):
            if ((mouse_x >= card1_5[0] and mouse_x <= card1_5[0] + card1_5[2]) and (mouse_y >= card1_5[1] and mouse_y <= card1_5[1] + card1_5[3])):
                pygame.draw.rect(game_board_disp, (200, 118, 144), card1_5, 0)
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    game_board_disp.blit(cards[21], (40,40))
            if (board_type[2][0] == 6):
                if ((mouse_x >= card1_6[0] and mouse_x <= card1_6[0] + card1_6[2]) and (mouse_y >= card1_6[1] and mouse_y <= card1_6[1] + card1_6[3])):
                    pygame.draw.rect(game_board_disp, (200, 118, 144), card1_6, 0)
                    if (pygame.mouse.get_pressed() == (1, 0, 0)):
                        game_board_disp.blit(cards[26], (40,40))
        # 2 row
        if ((mouse_x >= card2_1[0] and mouse_x <= card2_1[0] + card2_1[2]) and (mouse_y >= card2_1[1] and mouse_y <= card2_1[1] + card2_1[3])):
            pygame.draw.rect(game_board_disp, (200, 118, 144), card2_1, 0)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                game_board_disp.blit(cards[8], (40,40))

        if ((mouse_x >= card2_2[0] and mouse_x <= card2_2[0] + card2_2[2]) and (mouse_y >= card2_2[1] and mouse_y <= card2_2[1] + card2_2[3])):
            pygame.draw.rect(game_board_disp, (200, 118, 144), card2_2, 0)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                game_board_disp.blit(cards[9], (40,40))

        if ((mouse_x >= card2_3[0] and mouse_x <= card2_3[0] + card2_3[2]) and (mouse_y >= card2_3[1] and mouse_y <= card2_3[1] + card2_3[3])):
            pygame.draw.rect(game_board_disp, (200, 118, 144), card2_3, 0)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                game_board_disp.blit(cards[10], (40,40))

        if ((mouse_x >= card2_4[0] and mouse_x <= card2_4[0] + card2_4[2]) and (mouse_y >= card2_4[1] and mouse_y <= card2_4[1] + card2_4[3])):
            pygame.draw.rect(game_board_disp, (200, 118, 144), card2_4, 0)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                game_board_disp.blit(cards[11], (40,40))

        if (board_type[2][0] == 5 or board_type[2][0] == 6):
            if ((mouse_x >= card2_5[0] and mouse_x <= card2_5[0] + card2_5[2]) and (mouse_y >= card2_5[1] and mouse_y <= card2_5[1] + card2_5[3])):
                pygame.draw.rect(game_board_disp, (200, 118, 144), card2_5, 0)
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    game_board_disp.blit(cards[22], (40,40))
            if (board_type[2][0] == 6):
                if ((mouse_x >= card2_6[0] and mouse_x <= card2_6[0] + card2_6[2]) and (mouse_y >= card2_6[1] and mouse_y <= card2_6[1] + card2_6[3])):
                    pygame.draw.rect(game_board_disp, (200, 118, 144), card2_6, 0)
                    if (pygame.mouse.get_pressed() == (1, 0, 0)):
                        game_board_disp.blit(cards[27], (40,40))
        
        # 3 row
        if (board_type[2][1] == 4 or board_type[2][1] == 5 or board_type[2][1] == 6):
            if ((mouse_x >= card3_1[0] and mouse_x <= card3_1[0] + card3_1[2]) and (mouse_y >= card3_1[1] and mouse_y <= card3_1[1] + card3_1[3])):
                pygame.draw.rect(game_board_disp, (200, 118, 144), card3_1, 0)
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    game_board_disp.blit(cards[12], (40,40))

            if ((mouse_x >= card3_2[0] and mouse_x <= card3_2[0] + card3_2[2]) and (mouse_y >= card3_2[1] and mouse_y <= card3_2[1] + card3_2[3])):
                pygame.draw.rect(game_board_disp, (200, 118, 144), card3_2, 0)
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    game_board_disp.blit(cards[13], (40,40))

            if ((mouse_x >= card3_3[0] and mouse_x <= card3_3[0] + card3_3[2]) and (mouse_y >= card3_3[1] and mouse_y <= card3_3[1] + card3_3[3])):
                pygame.draw.rect(game_board_disp, (200, 118, 144), card3_3, 0)
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    game_board_disp.blit(cards[14], (40,40))

            if ((mouse_x >= card3_4[0] and mouse_x <= card3_4[0] + card3_4[2]) and (mouse_y >= card3_4[1] and mouse_y <= card3_4[1] + card3_4[3])):
                pygame.draw.rect(game_board_disp, (200, 118, 144), card3_4, 0)
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    game_board_disp.blit(cards[15], (40,40))
            
            if (board_type[2][0] == 5 or board_type[2][0] == 6):
                if ((mouse_x >= card3_5[0] and mouse_x <= card3_5[0] + card3_5[2]) and (mouse_y >= card3_5[1] and mouse_y <= card3_5[1] + card3_5[3])):
                    pygame.draw.rect(game_board_disp, (200, 118, 144), card3_5, 0)
                    if (pygame.mouse.get_pressed() == (1, 0, 0)):
                        game_board_disp.blit(cards[23], (40,40))
                if (board_type[2][0] == 6):
                    if ((mouse_x >= card3_6[0] and mouse_x <= card3_6[0] + card3_6[2]) and (mouse_y >= card3_6[1] and mouse_y <= card3_6[1] + card3_6[3])):
                        pygame.draw.rect(game_board_disp, (200, 118, 144), card3_6, 0)
                        if (pygame.mouse.get_pressed() == (1, 0, 0)):
                            game_board_disp.blit(cards[28], (40,40))
            # 4 row
            if (board_type[2][1] == 5 or board_type[2][1] == 6):
                if ((mouse_x >= card4_1[0] and mouse_x <= card4_1[0] + card4_1[2]) and (mouse_y >= card4_1[1] and mouse_y <= card4_1[1] + card4_1[3])):
                    pygame.draw.rect(game_board_disp, (200, 118, 144), card4_1, 0)
                    if (pygame.mouse.get_pressed() == (1, 0, 0)):
                        game_board_disp.blit(cards[16], (40,40))

                if ((mouse_x >= card4_2[0] and mouse_x <= card4_2[0] + card4_2[2]) and (mouse_y >= card4_2[1] and mouse_y <= card4_2[1] + card4_2[3])):
                    pygame.draw.rect(game_board_disp, (200, 118, 144), card4_2, 0)
                    if (pygame.mouse.get_pressed() == (1, 0, 0)):
                        game_board_disp.blit(cards[17], (40,40))

                if ((mouse_x >= card4_3[0] and mouse_x <= card4_3[0] + card4_3[2]) and (mouse_y >= card4_3[1] and mouse_y <= card4_3[1] + card4_3[3])):
                    pygame.draw.rect(game_board_disp, (200, 118, 144), card4_3, 0)
                    if (pygame.mouse.get_pressed() == (1, 0, 0)):
                        game_board_disp.blit(cards[18], (40,40))

                if ((mouse_x >= card4_4[0] and mouse_x <= card4_4[0] + card4_4[2]) and (mouse_y >= card4_4[1] and mouse_y <= card4_4[1] + card4_4[3])):
                    pygame.draw.rect(game_board_disp, (200, 118, 144), card4_4, 0)
                    if (pygame.mouse.get_pressed() == (1, 0, 0)):
                        game_board_disp.blit(cards[19], (40,40))
                
                if (board_type[2][0] == 5 or board_type[2][0] == 6):
                    if ((mouse_x >= card4_5[0] and mouse_x <= card4_5[0] + card4_5[2]) and (mouse_y >= card4_5[1] and mouse_y <= card4_5[1] + card4_5[3])):
                        pygame.draw.rect(game_board_disp, (200, 118, 144), card4_5, 0)
                        if (pygame.mouse.get_pressed() == (1, 0, 0)):
                            game_board_disp.blit(cards[24], (40,40))
                    if (board_type[2][0] == 6):
                        if ((mouse_x >= card4_6[0] and mouse_x <= card4_6[0] + card4_6[2]) and (mouse_y >= card4_6[1] and mouse_y <= card4_6[1] + card4_6[3])):
                            pygame.draw.rect(game_board_disp, (200, 118, 144), card4_6, 0)
                            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                                game_board_disp.blit(cards[29], (40,40))
                # 5 row
                if (board_type[2][1] == 6):
                    if ((mouse_x >= card5_1[0] and mouse_x <= card5_1[0] + card5_1[2]) and (mouse_y >= card5_1[1] and mouse_y <= card5_1[1] + card5_1[3])):
                        pygame.draw.rect(game_board_disp, (200, 118, 144), card5_1, 0)
                        if (pygame.mouse.get_pressed() == (1, 0, 0)):
                            game_board_disp.blit(cards[30], (40,40))

                    if ((mouse_x >= card5_2[0] and mouse_x <= card5_2[0] + card5_2[2]) and (mouse_y >= card5_2[1] and mouse_y <= card5_2[1] + card5_2[3])):
                        pygame.draw.rect(game_board_disp, (200, 118, 144), card5_2, 0)
                        if (pygame.mouse.get_pressed() == (1, 0, 0)):
                            game_board_disp.blit(cards[31], (40,40))

                    if ((mouse_x >= card5_3[0] and mouse_x <= card5_3[0] + card5_3[2]) and (mouse_y >= card5_3[1] and mouse_y <= card5_3[1] + card5_3[3])):
                        pygame.draw.rect(game_board_disp, (200, 118, 144), card5_3, 0)
                        if (pygame.mouse.get_pressed() == (1, 0, 0)):
                            game_board_disp.blit(cards[32], (40,40))

                    if ((mouse_x >= card5_4[0] and mouse_x <= card5_4[0] + card5_4[2]) and (mouse_y >= card5_4[1] and mouse_y <= card5_4[1] + card5_4[3])):
                        pygame.draw.rect(game_board_disp, (200, 118, 144), card5_4, 0)
                        if (pygame.mouse.get_pressed() == (1, 0, 0)):
                            game_board_disp.blit(cards[33], (40,40))
                    
                    if (board_type[2][0] == 5 or board_type[2][0] == 6):
                        if ((mouse_x >= card5_5[0] and mouse_x <= card5_5[0] + card5_5[2]) and (mouse_y >= card5_5[1] and mouse_y <= card5_5[1] + card5_5[3])):
                            pygame.draw.rect(game_board_disp, (200, 118, 144), card5_5, 0)
                            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                                game_board_disp.blit(cards[34], (40,40))
                        if (board_type[2][0] == 6):
                            if ((mouse_x >= card5_6[0] and mouse_x <= card5_6[0] + card5_6[2]) and (mouse_y >= card5_6[1] and mouse_y <= card5_6[1] + card5_6[3])):
                                pygame.draw.rect(game_board_disp, (200, 118, 144), card5_6, 0)
                                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                                    game_board_disp.blit(cards[35], (40,40))

        pygame.display.flip() 