import pygame
import pygame.freetype
import random
from board import board_menu
from options import options_menu

# Palete de cores em RGB:
# Rosa (232, 150, 167)
# Cinza (145, 146, 148)
# Cinza-Rosa (145, 118, 144)
# Vermelho-Rosa (129, 25, 55)
# Marrom-Rosa (45, 11, 23)

# Global variables
res = (1280, 720)

# The main function to run the program.
def main():
    pygame.init()

    # The start screen display
    screen_disp = pygame.display.set_mode(res)

    # The variables containing the fonts for the various text on screen_disp
    logo_font = pygame.freetype.Font("fonts/BMSPA__.TTF", (25, 65)) 
    credits_font = pygame.freetype.Font("fonts/BMSPA__.TTF", (15, 55))
    menu_font = logo_font = pygame.freetype.Font("fonts/BMSPA__.TTF", (25, 45))

    # The images 
    unmute = pygame.image.load("images/sound_sprite_unmute.png") 
    mute = pygame.image.load("images/sound_sprite_mute.png") 
    unmute_c = pygame.image.load("images/sound_sprite_unmutec.png") 
    mute_c = pygame.image.load("images/sound_sprite_mutec.png") 
    reimu = pygame.image.load("images/reimutest.png")
    start_bg = pygame.image.load("images/start_bg.png")

    # The sound effects
    click = pygame.mixer.Sound("sounds/normal_click.wav")
    back_click = pygame.mixer.Sound("sounds/back_click.wav")

    # The music track that will loop
    song = pygame.mixer.music
    song.load("sounds/Eternal-Shrine-Maiden.wav")

    # Plays the song and sets the boolean that determines it to True
    song.set_volume(0.5)
    song.play(-1)
    musicStatus = True

    # Variable that will determine if the mouse is in the mute button
    mouse_motion = False

    # The screen loop that updates frame-by-frame
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
                        pygame.time.delay(5)
                    else: 
                        song.unpause()
                        musicStatus = True
                        pygame.time.delay(5)
                elif (event.key == pygame.K_q):
                    exit()
            if (event.type == pygame.MOUSEMOTION):
                if ((event.pos[0] >= 20 and event.pos[0] <= 70) and (event.pos[1] >= 655 and event.pos[1] <= 705)):
                    mouse_motion = True
                else:
                    mouse_motion = False

        # Fills the screen with a color
        screen_disp.fill((0,10,0))

        # Draws the background and the main image
        screen_disp.blit(start_bg, (0, 0))
        screen_disp.blit(reimu, (1280 - 720, 0))
        
        # Renders the game text in the initial screen
        logo_font.render_to(screen_disp, (30, 30), "Gensokoyo Shuffle", (10, 10, 102), None, pygame.freetype.STYLE_OBLIQUE)
        logo_font.render_to(screen_disp, (20, 20), "Gensokoyo Shuffle", (100, 100, 232), None, pygame.freetype.STYLE_OBLIQUE)
        credits_font.render_to(screen_disp, (985, 590), "Made by Marco Domingos", (255, 255, 255))
        credits_font.render_to(screen_disp, (794, 655), "Music and Sprites by Team Shanghai Alice", (255, 255, 255))


        # Draws the 'Start' button rectangle and text
        rect_start = pygame.Rect(50, 120 - 25, 345, 50)
        pygame.draw.rect(screen_disp, (145, 118, 144), rect_start, 0)
        startText = "Start"
        menu_font.render_to(screen_disp, (50 + 172.5 - 50 , 95 + 25 - 17.5), startText, (129, 25, 55), None, pygame.freetype.STYLE_OBLIQUE)

        # Draws the 'Options' button rectangle and text
        rect_options = pygame.Rect(50, 200 - 25, 345, 50)
        pygame.draw.rect(screen_disp, (145, 118, 144), rect_options, 0)
        optionsText = "Options"
        menu_font.render_to(screen_disp, (50 + 172.5 - 68.5 , 175 + 26 - 22.5), optionsText, (129, 25, 55), None, pygame.freetype.STYLE_OBLIQUE)

        # Draws the images
        if (musicStatus):
            screen_disp.blit(unmute, (20, 655))
        else:
            screen_disp.blit(mute, (20, 655))

        # Gets the mouse position to determine clicks
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Verifies if player's mouse is inside the 'Start' rect and is clicked
        if ((mouse_x >= 50 and mouse_x <= 395) and (mouse_y >= 95 and mouse_y <= 145)):
            pygame.draw.rect(screen_disp, (200, 118, 144), rect_start, 0)
            menu_font.render_to(screen_disp, (50 + 172.5 - 50 , 95 + 25 - 17.5), startText, (149, 45, 75), None, pygame.freetype.STYLE_OBLIQUE)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                # Plays the 'click' SE
                click.play()

                # Delays the program
                pygame.time.delay(100)

                # Calls the board menu
                board_menu(song, click, back_click, musicStatus, res, unmute, mute, unmute_c, mute_c, mouse_motion)         

        # Verifies if player's mouse is inside the 'Options' rect and is clicked
        if ((mouse_x >= 50 and mouse_x <= 395) and (mouse_y >= 175 and mouse_y <= 225)):
            pygame.draw.rect(screen_disp, (200, 118, 144), rect_options, 0)
            menu_font.render_to(screen_disp, (50 + 172.5 - 68.5 , 175 + 26 - 22.5), optionsText, (149, 45, 75), None, pygame.freetype.STYLE_OBLIQUE)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                # Plays the 'click' SE
                click.play()

                # Delays the program
                pygame.time.delay(100)

                # Calls the board menu
                options_menu(song, click, back_click, musicStatus, res, mouse_x, mouse_y, unmute, mute, unmute_c, mute_c, mouse_motion)

        # Verifies if player's mouse is inside the mute button and mutes accordingly (NEED TO MAKE IT A FUNCTION, BUT DOES NOT RECEIVE SURFACE OF SCREEN)
        if (mouse_motion):
            if (musicStatus == True):
                screen_disp.blit(unmute_c, (20, 655))
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    song.pause()
                    musicStatus = False
                    pygame.time.delay(305)
            else: 
                screen_disp.blit(mute_c, (20, 655))
                if (pygame.mouse.get_pressed() == (1, 0, 0)):
                    song.unpause()
                    musicStatus = True
                    pygame.time.delay(305)

        # Flips the buffer display
        pygame.display.flip()

main()