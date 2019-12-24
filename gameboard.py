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

    # Observes the status of the click in order to verify which card was turned
    clickStatus = 40
    
    # Will determine if player flipped 1 or 2 cards
    cardVerif = 0

    # The variable that will store the players' points
    points = 0

    # The variable that will store the players' failed attempts and multiply it by the points
    tries = 0
    
    # The variable that will check if the player turned a second card and will freeze the display if True.
    dispflip = False

    # A list of booleans that will determine which cards have disappeared, and will be used to determine if the player won or not
    carddraw = []
    for jindex in range(0, board_type[0]):
        carddraw.append(True)
    
    # The positions and scales for each card, relative to the board chosen.
    cardres = [
        (1280/4, 20, 640/board_type[2][0], 680/board_type[2][1]),                                                           
        (1280/4 + 640/board_type[2][0], 20, 640/board_type[2][0], 680/board_type[2][1]),                                    
        (1280/4 + 2*(640/board_type[2][0]), 20, 640/board_type[2][0], 680/board_type[2][1]),                                
        (1280/4 + 3*(640/board_type[2][0]), 20, 640/board_type[2][0], 680/board_type[2][1]),                                
        (1280/4, 20 + 680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),                                    
        (1280/4 + 640/board_type[2][0], 20 + 680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),             
        (1280/4 + 2*(640/board_type[2][0]), 20 + 680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),         
        (1280/4 + 3*(640/board_type[2][0]), 20 + 680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),         
        (1280/4, 20 + 2*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),                                  
        (1280/4 + 640/board_type[2][0], 20 + 2*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),           
        (1280/4 + 2*(640/board_type[2][0]), 20 + 2*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),       
        (1280/4 + 3*(640/board_type[2][0]), 20 + 2*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),       
        (1280/4, 20 + 3*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),                                  
        (1280/4 + 640/board_type[2][0], 20 + 3*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),           
        (1280/4 + 2*(640/board_type[2][0]), 20 + 3*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),       
        (1280/4 + 3*(640/board_type[2][0]), 20 + 3*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),       
        (1280/4 + 4*(640/board_type[2][0]), 20, 640/board_type[2][0], 680/board_type[2][1]),                               
        (1280/4 + 4*(640/board_type[2][0]), 20 + 680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),        
        (1280/4 + 4*(640/board_type[2][0]), 20 + 2*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),      
        (1280/4 + 4*(640/board_type[2][0]), 20 + 3*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),      
        (1280/4 + 5*(640/board_type[2][0]), 20, 640/board_type[2][0], 680/board_type[2][1]),                               
        (1280/4 + 5*(640/board_type[2][0]), 20 + 680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),        
        (1280/4 + 5*(640/board_type[2][0]), 20 + 2*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),      
        (1280/4 + 5*(640/board_type[2][0]), 20 + 3*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),      
        (1280/4, 20 + 4*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),                                 
        (1280/4 + 640/board_type[2][0], 20 + 4*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),          
        (1280/4 + 2*(640/board_type[2][0]), 20 + 4*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),      
        (1280/4 + 3*(640/board_type[2][0]), 20 + 4*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),      
        (1280/4 + 4*(640/board_type[2][0]), 20 + 4*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),      
        (1280/4 + 5*(640/board_type[2][0]), 20 + 4*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),       
        (1280/4, 20 + 5*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),                                  
        (1280/4 + 640/board_type[2][0], 20 + 5*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),           
        (1280/4 + 2*(640/board_type[2][0]), 20 + 5*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),       
        (1280/4 + 3*(640/board_type[2][0]), 20 + 5*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),       
        (1280/4 + 4*(640/board_type[2][0]), 20 + 5*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1]),       
        (1280/4 + 5*(640/board_type[2][0]), 20 + 5*680/board_type[2][1], 640/board_type[2][0], 680/board_type[2][1])        
    ]

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
                        print(str(carddraw))
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

        # Renders the 'points' text and value
        pointsText = "Points:"
        pointsValue = str(points)
        game_board_font.render_to(game_board_disp, (25, 25), pointsText, (102, 30, 47), None, pygame.freetype.STYLE_OBLIQUE)
        game_board_font.render_to(game_board_disp, (20, 20), pointsText, (232, 150, 167), None, pygame.freetype.STYLE_OBLIQUE)
        game_board_font.render_to(game_board_disp, (115, 25), pointsValue, (102, 30, 47), None, pygame.freetype.STYLE_OBLIQUE)
        game_board_font.render_to(game_board_disp, (110, 20), pointsValue, (232, 150, 167), None, pygame.freetype.STYLE_OBLIQUE)
        
        # Renders the victory message
        if (not any(carddraw)):
            congratz = "Congratulations!"
            congratzSize = game_board_font.get_rect(congratz)
            game_board_font.render_to(game_board_disp, (645 - congratzSize[2]/2, 365 - congratzSize[3]/2), congratz, (102, 30, 47))
            game_board_font.render_to(game_board_disp, (640 - congratzSize[2]/2, 360 - congratzSize[3]/2), congratz, (232, 150, 167))

        # Draws the horizontal cards in the specific board
        # 0 row
        card0_1 = pygame.Rect(cardres[0][0], cardres[0][1], cardres[0][2], cardres[0][3]) ##
        if(carddraw[0]):
            pygame.draw.rect(game_board_disp, (129, 25, 55), card0_1, 1)

        card0_2 = pygame.Rect(cardres[1][0], cardres[1][1], cardres[1][2], cardres[1][3]) ##
        if(carddraw[1]):
            pygame.draw.rect(game_board_disp, (129, 25, 55), card0_2, 1)

        card0_3 = pygame.Rect(cardres[2][0], cardres[2][1], cardres[2][2], cardres[2][3]) ##
        if(carddraw[2]):
            pygame.draw.rect(game_board_disp, (129, 25, 55), card0_3, 1)

        card0_4 = pygame.Rect(cardres[3][0], cardres[3][1], cardres[3][2], cardres[3][3]) ##
        if(carddraw[3]):
            pygame.draw.rect(game_board_disp, (129, 25, 55), card0_4, 1)

        if(board_type[2][0] == 5 or board_type[2][0] == 6):
            card0_5 = pygame.Rect(cardres[16][0], cardres[16][1], cardres[16][2], cardres[16][3]) ##
            if(carddraw[16]):
                pygame.draw.rect(game_board_disp, (129, 25, 55), card0_5, 1)
            if(board_type[2][0] == 6):
                card0_6 = pygame.Rect(cardres[20][0], cardres[20][1], cardres[20][2], cardres[20][3]) ##
                if(carddraw[20]):
                    pygame.draw.rect(game_board_disp, (129, 25, 55), card0_6, 1)
            
        # 1 row
        card1_1 = pygame.Rect(cardres[4][0], cardres[4][1], cardres[4][2], cardres[4][3]) ##
        if(carddraw[4]):
            pygame.draw.rect(game_board_disp, (129, 25, 55), card1_1, 1)
        
        card1_2 = pygame.Rect(cardres[5][0], cardres[5][1], cardres[5][2], cardres[5][3]) ##
        if(carddraw[5]):
            pygame.draw.rect(game_board_disp, (129, 25, 55), card1_2, 1)

        card1_3 = pygame.Rect(cardres[6][0], cardres[6][1], cardres[6][2], cardres[6][3]) ##
        if(carddraw[6]):
            pygame.draw.rect(game_board_disp, (129, 25, 55), card1_3, 1)

        card1_4 = pygame.Rect(cardres[7][0], cardres[7][1], cardres[7][2], cardres[7][3]) ##
        if(carddraw[7]):
            pygame.draw.rect(game_board_disp, (129, 25, 55), card1_4, 1)

        if(board_type[2][0] == 5 or board_type[2][0] == 6):
            card1_5 = pygame.Rect(cardres[17][0], cardres[17][1], cardres[17][2], cardres[17][3]) ##
            if(carddraw[17]):
                pygame.draw.rect(game_board_disp, (129, 25, 55), card1_5, 1)
            if(board_type[2][0] == 6):
                card1_6 = pygame.Rect(cardres[21][0], cardres[21][1], cardres[21][2], cardres[21][3]) ##
                if(carddraw[21]):
                    pygame.draw.rect(game_board_disp, (129, 25, 55), card1_6, 1)

        # 2 row
        card2_1 = pygame.Rect(cardres[8][0], cardres[8][1], cardres[8][2], cardres[8][3]) ##
        if(carddraw[8]):
            pygame.draw.rect(game_board_disp, (129, 25, 55), card2_1, 1)

        card2_2 = pygame.Rect(cardres[9][0], cardres[9][1], cardres[9][2], cardres[9][3]) ##
        if(carddraw[9]):
            pygame.draw.rect(game_board_disp, (129, 25, 55), card2_2, 1)

        card2_3 = pygame.Rect(cardres[10][0], cardres[10][1], cardres[10][2], cardres[10][3]) ##
        if(carddraw[10]):
            pygame.draw.rect(game_board_disp, (129, 25, 55), card2_3, 1)

        card2_4 = pygame.Rect(cardres[11][0], cardres[11][1], cardres[11][2], cardres[11][3]) ##
        if(carddraw[11]):
            pygame.draw.rect(game_board_disp, (129, 25, 55), card2_4, 1)

        if(board_type[2][0] == 5 or board_type[2][0] == 6):
            card2_5 = pygame.Rect(cardres[18][0], cardres[18][1], cardres[18][2], cardres[18][3]) ##
            if(carddraw[18]):
                pygame.draw.rect(game_board_disp, (129, 25, 55), card2_5, 1)
            if(board_type[2][0] == 6):
                card2_6 = pygame.Rect(cardres[22][0], cardres[22][1], cardres[22][2], cardres[22][3]) ##
                if(carddraw[22]):
                    pygame.draw.rect(game_board_disp, (129, 25, 55), card2_6, 1)

        # 3 row
        if(board_type[2][1] == 4 or board_type[2][1] == 5 or board_type[2][1] == 6):
            card3_1 = pygame.Rect(cardres[12][0], cardres[12][1], cardres[12][2], cardres[12][3]) ##
            if(carddraw[12]):
                pygame.draw.rect(game_board_disp, (129, 25, 55), card3_1, 1)

            card3_2 = pygame.Rect(cardres[13][0], cardres[13][1], cardres[13][2], cardres[13][3]) ##
            if(carddraw[13]):
                pygame.draw.rect(game_board_disp, (129, 25, 55), card3_2, 1)

            card3_3 = pygame.Rect(cardres[14][0], cardres[14][1], cardres[14][2], cardres[14][3]) ##
            if(carddraw[14]):
                pygame.draw.rect(game_board_disp, (129, 25, 55), card3_3, 1)

            card3_4 = pygame.Rect(cardres[15][0], cardres[15][1], cardres[15][2], cardres[15][3]) ##
            if(carddraw[15]):
                pygame.draw.rect(game_board_disp, (129, 25, 55), card3_4, 1)

            if(board_type[2][0] == 5 or board_type[2][0] == 6):
                card3_5 = pygame.Rect(cardres[19][0], cardres[19][1], cardres[19][2], cardres[19][3]) ##
                if(carddraw[19]):
                    pygame.draw.rect(game_board_disp, (129, 25, 55), card3_5, 1)
                if(board_type[2][0] == 6):
                    card3_6 = pygame.Rect(cardres[23][0], cardres[23][1], cardres[23][2], cardres[23][3]) ##
                    if(carddraw[23]):
                        pygame.draw.rect(game_board_disp, (129, 25, 55), card3_6, 1)

            # 4 row    
            if(board_type[2][1] == 5 or board_type[2][1] == 6):
                card4_1 = pygame.Rect(cardres[24][0], cardres[24][1], cardres[24][2], cardres[24][3]) ##
                if(carddraw[24]):
                    pygame.draw.rect(game_board_disp, (129, 25, 55), card4_1, 1)

                card4_2 = pygame.Rect(cardres[25][0], cardres[25][1], cardres[25][2], cardres[25][3]) ##
                if(carddraw[25]):
                    pygame.draw.rect(game_board_disp, (129, 25, 55), card4_2, 1)

                card4_3 = pygame.Rect(cardres[26][0], cardres[26][1], cardres[26][2], cardres[26][3]) ##
                if(carddraw[26]):
                    pygame.draw.rect(game_board_disp, (129, 25, 55), card4_3, 1)

                card4_4 = pygame.Rect(cardres[27][0], cardres[27][1], cardres[27][2], cardres[27][3]) ##
                if(carddraw[27]):
                    pygame.draw.rect(game_board_disp, (129, 25, 55), card4_4, 1)

                if(board_type[2][0] == 5 or board_type[2][0] == 6):
                    card4_5 = pygame.Rect(cardres[28][0], cardres[28][1], cardres[28][2], cardres[28][3]) ##
                    if(carddraw[28]):
                        pygame.draw.rect(game_board_disp, (129, 25, 55), card4_5, 1)
                    if (board_type[2][0] == 6):
                        card4_6 = pygame.Rect(cardres[29][0], cardres[29][1], cardres[29][2], cardres[29][3]) ##
                        if(carddraw[29]):
                            pygame.draw.rect(game_board_disp, (129, 25, 55), card4_6, 1)

                # 5 row
                if(board_type[2][1] == 6):
                    card5_1 = pygame.Rect(cardres[30][0], cardres[30][1], cardres[30][2], cardres[30][3]) ##
                    if(carddraw[30]):
                        pygame.draw.rect(game_board_disp, (129, 25, 55), card5_1, 1)

                    card5_2 = pygame.Rect(cardres[31][0], cardres[31][1], cardres[31][2], cardres[31][3]) ##
                    if(carddraw[31]):
                        pygame.draw.rect(game_board_disp, (129, 25, 55), card5_2, 1)

                    card5_3 = pygame.Rect(cardres[32][0], cardres[32][1], cardres[32][2], cardres[32][3]) ##
                    if(carddraw[32]):
                        pygame.draw.rect(game_board_disp, (129, 25, 55), card5_3, 1)

                    card5_4 = pygame.Rect(cardres[33][0], cardres[33][1], cardres[33][2], cardres[33][3]) ##
                    if(carddraw[33]):
                        pygame.draw.rect(game_board_disp, (129, 25, 55), card5_4, 1)

                    if(board_type[2][0] == 5 or board_type[2][0] == 6):
                        card5_5 = pygame.Rect(cardres[34][0], cardres[34][1], cardres[34][2], cardres[34][3]) ##
                        if(carddraw[34]):
                            pygame.draw.rect(game_board_disp, (129, 25, 55), card5_5, 1)
                        if(board_type[2][0] == 6):
                            card5_6 = pygame.Rect(cardres[35][0], cardres[35][1], cardres[35][2], cardres[35][3]) ##
                            if(carddraw[35]):
                                pygame.draw.rect(game_board_disp, (129, 25, 55), card5_6, 1)

        # Draws the points

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
                return musicStatus
        
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
        if ((mouse_x >= card0_1[0] and mouse_x <= card0_1[0] + card0_1[2]) and (mouse_y >= card0_1[1] and mouse_y <= card0_1[1] + card0_1[3]) and (clickStatus != 0) and carddraw[0]):
            pygame.draw.rect(game_board_disp, (200, 118, 144), card0_1, 0)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                clickStatus = 0 
                cardVerif += 1
                pygame.time.wait(60)

        if ((mouse_x >= card0_2[0] and mouse_x <= card0_2[0] + card0_2[2]) and (mouse_y >= card0_2[1] and mouse_y <= card0_2[1] + card0_2[3]) and (clickStatus != 1) and carddraw[1]):
            pygame.draw.rect(game_board_disp, (200, 118, 144), card0_2, 0)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                clickStatus = 1
                cardVerif += 1
                pygame.time.wait(60)

        if ((mouse_x >= card0_3[0] and mouse_x <= card0_3[0] + card0_3[2]) and (mouse_y >= card0_3[1] and mouse_y <= card0_3[1] + card0_3[3]) and (clickStatus != 2) and carddraw[2]):
            pygame.draw.rect(game_board_disp, (200, 118, 144), card0_3, 0)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                clickStatus = 2
                cardVerif += 1
                pygame.time.wait(60)

        if ((mouse_x >= card0_4[0] and mouse_x <= card0_4[0] + card0_4[2]) and (mouse_y >= card0_4[1] and mouse_y <= card0_4[1] + card0_4[3]) and (clickStatus != 3) and carddraw[3]):
            pygame.draw.rect(game_board_disp, (200, 118, 144), card0_4, 0)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                clickStatus = 3
                cardVerif += 1
                pygame.time.wait(60)
        
        if (board_type[2][0] == 5 or board_type[2][0] == 6):
            if ((mouse_x >= card0_5[0] and mouse_x <= card0_5[0] + card0_5[2]) and (mouse_y >= card0_5[1] and mouse_y <= card0_5[1] + card0_5[3]) and (clickStatus != 16) and carddraw[16]):
                pygame.draw.rect(game_board_disp, (200, 118, 144), card0_5, 0)
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    clickStatus = 16
                    cardVerif += 1
                    pygame.time.wait(60)
            if (board_type[2][0] == 6):
                if ((mouse_x >= card0_6[0] and mouse_x <= card0_6[0] + card0_6[2]) and (mouse_y >= card0_6[1] and mouse_y <= card0_6[1] + card0_6[3]) and (clickStatus != 20) and carddraw[20]):
                    pygame.draw.rect(game_board_disp, (200, 118, 144), card0_6, 0)
                    if (pygame.mouse.get_pressed() == (1, 0, 0)):
                        clickStatus = 20
                        cardVerif += 1
                        pygame.time.wait(60)

        # 1 row
        if ((mouse_x >= card1_1[0] and mouse_x <= card1_1[0] + card1_1[2]) and (mouse_y >= card1_1[1] and mouse_y <= card1_1[1] + card1_1[3]) and (clickStatus != 4) and carddraw[4]):
            pygame.draw.rect(game_board_disp, (200, 118, 144), card1_1, 0)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                clickStatus = 4
                cardVerif += 1
                pygame.time.wait(60)

        if ((mouse_x >= card1_2[0] and mouse_x <= card1_2[0] + card1_2[2]) and (mouse_y >= card1_2[1] and mouse_y <= card1_2[1] + card1_2[3]) and (clickStatus != 5) and carddraw[5]):
            pygame.draw.rect(game_board_disp, (200, 118, 144), card1_2, 0)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                clickStatus = 5
                cardVerif += 1
                pygame.time.wait(60)

        if ((mouse_x >= card1_3[0] and mouse_x <= card1_3[0] + card1_3[2]) and (mouse_y >= card1_3[1] and mouse_y <= card1_3[1] + card1_3[3]) and (clickStatus != 6) and carddraw[6]):
            pygame.draw.rect(game_board_disp, (200, 118, 144), card1_3, 0)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                clickStatus = 6
                cardVerif += 1
                pygame.time.wait(60)
        
        if ((mouse_x >= card1_4[0] and mouse_x <= card1_4[0] + card1_4[2]) and (mouse_y >= card1_4[1] and mouse_y <= card1_4[1] + card1_4[3]) and (clickStatus != 7) and carddraw[7]):
            pygame.draw.rect(game_board_disp, (200, 118, 144), card1_4, 0)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                clickStatus = 7
                cardVerif += 1
                pygame.time.wait(60)

        if (board_type[2][0] == 5 or board_type[2][0] == 6):
            if ((mouse_x >= card1_5[0] and mouse_x <= card1_5[0] + card1_5[2]) and (mouse_y >= card1_5[1] and mouse_y <= card1_5[1] + card1_5[3]) and (clickStatus != 17) and carddraw[17]):
                pygame.draw.rect(game_board_disp, (200, 118, 144), card1_5, 0)
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    clickStatus = 17
                    cardVerif += 1
                    pygame.time.wait(60)
            if (board_type[2][0] == 6):
                if ((mouse_x >= card1_6[0] and mouse_x <= card1_6[0] + card1_6[2]) and (mouse_y >= card1_6[1] and mouse_y <= card1_6[1] + card1_6[3]) and (clickStatus != 21) and carddraw[21]):
                    pygame.draw.rect(game_board_disp, (200, 118, 144), card1_6, 0)
                    if (pygame.mouse.get_pressed() == (1, 0, 0)):
                        clickStatus = 21
                        cardVerif += 1
                        pygame.time.wait(60)
        # 2 row
        if ((mouse_x >= card2_1[0] and mouse_x <= card2_1[0] + card2_1[2]) and (mouse_y >= card2_1[1] and mouse_y <= card2_1[1] + card2_1[3]) and (clickStatus != 8) and carddraw[8]):
            pygame.draw.rect(game_board_disp, (200, 118, 144), card2_1, 0)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                clickStatus = 8
                cardVerif += 1
                pygame.time.wait(60)

        if ((mouse_x >= card2_2[0] and mouse_x <= card2_2[0] + card2_2[2]) and (mouse_y >= card2_2[1] and mouse_y <= card2_2[1] + card2_2[3]) and (clickStatus != 9) and carddraw[9]):
            pygame.draw.rect(game_board_disp, (200, 118, 144), card2_2, 0)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                clickStatus = 9
                cardVerif += 1
                pygame.time.wait(60)

        if ((mouse_x >= card2_3[0] and mouse_x <= card2_3[0] + card2_3[2]) and (mouse_y >= card2_3[1] and mouse_y <= card2_3[1] + card2_3[3]) and (clickStatus != 10) and carddraw[10]):
            pygame.draw.rect(game_board_disp, (200, 118, 144), card2_3, 0)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                clickStatus = 10
                cardVerif += 1
                pygame.time.wait(60)

        if ((mouse_x >= card2_4[0] and mouse_x <= card2_4[0] + card2_4[2]) and (mouse_y >= card2_4[1] and mouse_y <= card2_4[1] + card2_4[3]) and (clickStatus != 11) and carddraw[11]):
            pygame.draw.rect(game_board_disp, (200, 118, 144), card2_4, 0)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                clickStatus = 11
                cardVerif += 1
                pygame.time.wait(60)

        if (board_type[2][0] == 5 or board_type[2][0] == 6):
            if ((mouse_x >= card2_5[0] and mouse_x <= card2_5[0] + card2_5[2]) and (mouse_y >= card2_5[1] and mouse_y <= card2_5[1] + card2_5[3]) and (clickStatus != 18) and carddraw[18]):
                pygame.draw.rect(game_board_disp, (200, 118, 144), card2_5, 0)
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    clickStatus = 18
                    cardVerif += 1
                    pygame.time.wait(60)
            if (board_type[2][0] == 6):
                if ((mouse_x >= card2_6[0] and mouse_x <= card2_6[0] + card2_6[2]) and (mouse_y >= card2_6[1] and mouse_y <= card2_6[1] + card2_6[3]) and (clickStatus != 22) and carddraw[22]):
                    pygame.draw.rect(game_board_disp, (200, 118, 144), card2_6, 0)
                    if (pygame.mouse.get_pressed() == (1, 0, 0)):
                        clickStatus = 22
                        cardVerif += 1
                        pygame.time.wait(60)
        
        # 3 row
        if (board_type[2][1] == 4 or board_type[2][1] == 5 or board_type[2][1] == 6):
            if ((mouse_x >= card3_1[0] and mouse_x <= card3_1[0] + card3_1[2]) and (mouse_y >= card3_1[1] and mouse_y <= card3_1[1] + card3_1[3]) and (clickStatus != 12) and carddraw[12]):
                pygame.draw.rect(game_board_disp, (200, 118, 144), card3_1, 0)
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    clickStatus = 12
                    cardVerif += 1
                    pygame.time.wait(60)

            if ((mouse_x >= card3_2[0] and mouse_x <= card3_2[0] + card3_2[2]) and (mouse_y >= card3_2[1] and mouse_y <= card3_2[1] + card3_2[3]) and (clickStatus != 13) and carddraw[13]):
                pygame.draw.rect(game_board_disp, (200, 118, 144), card3_2, 0)
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    clickStatus = 13
                    cardVerif += 1
                    pygame.time.wait(60)

            if ((mouse_x >= card3_3[0] and mouse_x <= card3_3[0] + card3_3[2]) and (mouse_y >= card3_3[1] and mouse_y <= card3_3[1] + card3_3[3]) and (clickStatus != 14) and carddraw[14]):
                pygame.draw.rect(game_board_disp, (200, 118, 144), card3_3, 0)
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    clickStatus = 14
                    cardVerif += 1
                    pygame.time.wait(60)

            if ((mouse_x >= card3_4[0] and mouse_x <= card3_4[0] + card3_4[2]) and (mouse_y >= card3_4[1] and mouse_y <= card3_4[1] + card3_4[3]) and (clickStatus != 15) and carddraw[15]):
                pygame.draw.rect(game_board_disp, (200, 118, 144), card3_4, 0)
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    clickStatus = 15
                    cardVerif += 1
                    pygame.time.wait(60)
            
            if (board_type[2][0] == 5 or board_type[2][0] == 6):
                if ((mouse_x >= card3_5[0] and mouse_x <= card3_5[0] + card3_5[2]) and (mouse_y >= card3_5[1] and mouse_y <= card3_5[1] + card3_5[3]) and (clickStatus != 19) and carddraw[19]):
                    pygame.draw.rect(game_board_disp, (200, 118, 144), card3_5, 0)
                    if (pygame.mouse.get_pressed() == (1, 0, 0)):
                        clickStatus = 19
                        cardVerif += 1
                        pygame.time.wait(60)
                if (board_type[2][0] == 6):
                    if ((mouse_x >= card3_6[0] and mouse_x <= card3_6[0] + card3_6[2]) and (mouse_y >= card3_6[1] and mouse_y <= card3_6[1] + card3_6[3]) and (clickStatus != 23) and carddraw[23]):
                        pygame.draw.rect(game_board_disp, (200, 118, 144), card3_6, 0)
                        if (pygame.mouse.get_pressed() == (1, 0, 0)):
                            clickStatus = 23
                            cardVerif += 1              
                            pygame.time.wait(60)
            # 4 row
            if (board_type[2][1] == 5 or board_type[2][1] == 6):
                if ((mouse_x >= card4_1[0] and mouse_x <= card4_1[0] + card4_1[2]) and (mouse_y >= card4_1[1] and mouse_y <= card4_1[1] + card4_1[3]) and (clickStatus != 24) and carddraw[24]):
                    pygame.draw.rect(game_board_disp, (200, 118, 144), card4_1, 0)
                    if (pygame.mouse.get_pressed() == (1, 0, 0)):
                        clickStatus = 24
                        cardVerif += 1
                        pygame.time.wait(60)

                if ((mouse_x >= card4_2[0] and mouse_x <= card4_2[0] + card4_2[2]) and (mouse_y >= card4_2[1] and mouse_y <= card4_2[1] + card4_2[3]) and (clickStatus != 25) and carddraw[25]):
                    pygame.draw.rect(game_board_disp, (200, 118, 144), card4_2, 0)
                    if (pygame.mouse.get_pressed() == (1, 0, 0)):
                        clickStatus = 25
                        cardVerif += 1
                        pygame.time.wait(60)

                if ((mouse_x >= card4_3[0] and mouse_x <= card4_3[0] + card4_3[2]) and (mouse_y >= card4_3[1] and mouse_y <= card4_3[1] + card4_3[3]) and (clickStatus != 26) and carddraw[26]):
                    pygame.draw.rect(game_board_disp, (200, 118, 144), card4_3, 0)
                    if (pygame.mouse.get_pressed() == (1, 0, 0)):
                        clickStatus = 26
                        cardVerif += 1
                        pygame.time.wait(60)

                if ((mouse_x >= card4_4[0] and mouse_x <= card4_4[0] + card4_4[2]) and (mouse_y >= card4_4[1] and mouse_y <= card4_4[1] + card4_4[3]) and (clickStatus != 27) and carddraw[27]):
                    pygame.draw.rect(game_board_disp, (200, 118, 144), card4_4, 0)
                    if (pygame.mouse.get_pressed() == (1, 0, 0)):
                        clickStatus = 27
                        cardVerif += 1
                        pygame.time.wait(60)
                
                if (board_type[2][0] == 5 or board_type[2][0] == 6):
                    if ((mouse_x >= card4_5[0] and mouse_x <= card4_5[0] + card4_5[2]) and (mouse_y >= card4_5[1] and mouse_y <= card4_5[1] + card4_5[3]) and (clickStatus != 24) and carddraw[24]):
                        pygame.draw.rect(game_board_disp, (200, 118, 144), card4_5, 0)
                        if (pygame.mouse.get_pressed() == (1, 0, 0)):
                            clickStatus = 28
                            cardVerif += 1
                            pygame.time.wait(60)
                    if (board_type[2][0] == 6):
                        if ((mouse_x >= card4_6[0] and mouse_x <= card4_6[0] + card4_6[2]) and (mouse_y >= card4_6[1] and mouse_y <= card4_6[1] + card4_6[3]) and (clickStatus != 29) and carddraw[29]):
                            pygame.draw.rect(game_board_disp, (200, 118, 144), card4_6, 0)
                            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                                clickStatus = 29
                                cardVerif += 1
                                pygame.time.wait(60)
                # 5 row
                if (board_type[2][1] == 6):
                    if ((mouse_x >= card5_1[0] and mouse_x <= card5_1[0] + card5_1[2]) and (mouse_y >= card5_1[1] and mouse_y <= card5_1[1] + card5_1[3]) and (clickStatus != 30) and carddraw[30]):
                        pygame.draw.rect(game_board_disp, (200, 118, 144), card5_1, 0)
                        if (pygame.mouse.get_pressed() == (1, 0, 0)):
                            clickStatus = 30
                            cardVerif += 1
                            pygame.time.wait(60)

                    if ((mouse_x >= card5_2[0] and mouse_x <= card5_2[0] + card5_2[2]) and (mouse_y >= card5_2[1] and mouse_y <= card5_2[1] + card5_2[3]) and (clickStatus != 31) and carddraw[31]):
                        pygame.draw.rect(game_board_disp, (200, 118, 144), card5_2, 0)
                        if (pygame.mouse.get_pressed() == (1, 0, 0)):
                            clickStatus = 31
                            cardVerif += 1
                            pygame.time.wait(60)

                    if ((mouse_x >= card5_3[0] and mouse_x <= card5_3[0] + card5_3[2]) and (mouse_y >= card5_3[1] and mouse_y <= card5_3[1] + card5_3[3]) and (clickStatus != 32) and carddraw[32]):
                        pygame.draw.rect(game_board_disp, (200, 118, 144), card5_3, 0)
                        if (pygame.mouse.get_pressed() == (1, 0, 0)):
                            clickStatus = 32
                            cardVerif += 1
                            pygame.time.wait(60)

                    if ((mouse_x >= card5_4[0] and mouse_x <= card5_4[0] + card5_4[2]) and (mouse_y >= card5_4[1] and mouse_y <= card5_4[1] + card5_4[3]) and (clickStatus != 33) and carddraw[33]):
                        pygame.draw.rect(game_board_disp, (200, 118, 144), card5_4, 0)
                        if (pygame.mouse.get_pressed() == (1, 0, 0)):
                            clickStatus = 33
                            cardVerif += 1
                            pygame.time.wait(60)
                    
                    if (board_type[2][0] == 5 or board_type[2][0] == 6):
                        if ((mouse_x >= card5_5[0] and mouse_x <= card5_5[0] + card5_5[2]) and (mouse_y >= card5_5[1] and mouse_y <= card5_5[1] + card5_5[3]) and (clickStatus != 34) and carddraw[34]):
                            pygame.draw.rect(game_board_disp, (200, 118, 144), card5_5, 0)
                            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                                clickStatus = 34
                                cardVerif += 1
                                pygame.time.wait(60)
                        if (board_type[2][0] == 6):
                            if ((mouse_x >= card5_6[0] and mouse_x <= card5_6[0] + card5_6[2]) and (mouse_y >= card5_6[1] and mouse_y <= card5_6[1] + card5_6[3]) and (clickStatus != 35) and carddraw[35]):
                                pygame.draw.rect(game_board_disp, (200, 118, 144), card5_6, 0)
                                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                                    clickStatus = 35
                                    cardVerif += 1
                                    pygame.time.wait(60)
        
        if (cardVerif == 1):
            clickFirstCard = clickStatus
            game_board_disp.blit(cards[clickFirstCard], (cardres[clickFirstCard][0] + (cardres[clickFirstCard][2]/2) - 22, cardres[clickFirstCard][1] + (cardres[clickFirstCard][3]/2) - 21))

        if (cardVerif == 2):
            game_board_disp.blit(cards[clickFirstCard], (cardres[clickFirstCard][0] + (cardres[clickFirstCard][2]/2) - 22, cardres[clickFirstCard][1] + (cardres[clickFirstCard][3]/2) - 21))
            game_board_disp.blit(cards[clickStatus], (cardres[clickStatus][0] + (cardres[clickStatus][2]/2) - 22, cardres[clickStatus][1] + (cardres[clickStatus][3]/2) - 21))
            dispflip = True
            if (cards[clickFirstCard] == cards[clickStatus]):
                points += 100
                carddraw[clickFirstCard] = False
                carddraw[clickStatus] = False
                clickStatus = 40
                cardVerif = 0
            else:
                tries += 1
                points -= 20 * tries
                if (points < 0):
                    points = 0
                clickStatus = 40
                cardVerif = 0

        pygame.display.flip()

        if (dispflip):
            pygame.time.delay(1000)
            dispflip = False