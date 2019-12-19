import pygame
import pygame.freetype
import random

# Global variables
res = (1280, 720)

# The main function to run the program.
def main():
    pygame.init()

    screen_disp = pygame.display.set_mode(res)
    test_font = pygame.freetype.Font("ADOBEARABIC-ITALIC.OTF", 65)
    test_font2 = pygame.freetype.Font("ADOBEARABIC-REGULAR.OTF", 35)

    # The screen loop that updates frame-by-frame
    while(True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()

        screen_disp.fill((0,10,0))

        # Renders the game text in the initial screen
        test_font.render_to(screen_disp, (20, 20), "Gensokoyo Shuffle", (10, 10, 255))
        test_font2.render_to(screen_disp, (975, 700 - 20), "Made by Marco Domingos", (255, 255, 255))

        # Draws the 'Start' button rectangle
        rect_start = pygame.Rect(50, 120 - 25, 345, 50)
        pygame.draw.rect(screen_disp, (100, 10, 0), rect_start, 0)

        # Draws the 'Options' button rectangle
        rect_options = pygame.Rect(50, 200 - 25, 345, 50)
        pygame.draw.rect(screen_disp, (100, 10, 0), rect_options, 0)

        # Gets the mouse position to determine clicks
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Verifies if player's mouse is inside the 'Start' rect and is clicked
        if ((mouse_x >= 50 and mouse_x <= 395) and (mouse_y >= 95 and mouse_y <= 145)):
            pygame.draw.rect(screen_disp, (255, 10, 0), rect_start, 0)
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                get_board_size()

        # Verifies if player's mouse is inside the 'Options' rect and is clicked
        if ((mouse_x >= 50 and mouse_x <= 395) and (mouse_y >= 175 and mouse_y <= 225)):
            pygame.draw.rect(screen_disp, (255, 10, 0), rect_options, 0)

        # Flips the buffer display
        pygame.display.flip()

# Function that defines the display of the board dimension selection
def get_board_size():

    board_select_disp = pygame.display.set_mode(res)
    test_font3 = pygame.freetype.Font("ADOBEARABIC-REGULAR.OTF", 35)

    while(True):
        # Fills the screen 
        board_select_disp.fill((0,10,0))

        # Observes if the player quits
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
            
        # Gets the rectangle of the text and uses it to center the text in the screen
        optionText = "Select your board!"
        selectText = test_font3.get_rect(optionText)
        test_font3.render_to(board_select_disp, (640 - (selectText[2] / 2) , 20), optionText, (10, 10, 255))

        # Draws the 4x3 rectangle option
        rect_4x3 = pygame.Rect(640 - 172.5, 120, 345, 50)
        pygame.draw.rect(board_select_disp, (100, 10, 0), rect_4x3, 0)
        
        # Draws the 4x4 rectangle option
        rect_4x4 = pygame.Rect(640 - 172.5, 200, 345, 50)
        pygame.draw.rect(board_select_disp, (100, 10, 0), rect_4x4, 0)

        # Draws the 5x4 rectangle option
        rect_5x4 = pygame.Rect(640 - 172.5, 280, 345, 50)
        pygame.draw.rect(board_select_disp, (100, 10, 0), rect_5x4, 0)

        # Draws the 6x5 rectangle option
        rect_6x5 = pygame.Rect(640 - 172.5, 360, 345, 50)
        pygame.draw.rect(board_select_disp, (100, 10, 0), rect_6x5, 0)

        # Draws the 6x6 rectangle option
        rect_6x6 = pygame.Rect(640 - 172.5, 440, 345, 50)
        pygame.draw.rect(board_select_disp, (100, 10, 0), rect_6x6, 0)

        pygame.display.flip()
        
    
main()