import pygame
#general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
BG = (25, 28, 40)
PLAYER_COLOR = (120, 220, 170)
COIN_COLOR = (245, 202, 87)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("snake_labs")

#game setup

#import images
player_sprite = pygame.image.load("images/player.png")
player_sprite = player_sprite.convert_alpha()
player_sprite = pygame.transform.scale(player_sprite, (100,100))
player_sprite = pygame.transform.rotate(player_sprite, 45)

player = player_sprite.get_frect( center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
running = True
while running:
    #---------------------------------------------------
    # Timekeeping
    #---------------------------------------------------

    dt = pygame.time.Clock().tick(60)/1000  # Delta time in seconds
    #---------------------------------------------------
    # Event loop
    #---------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    #---------------------------------------------------
    # End of event loop
    #---------------------------------------------------

    #---------------------------------------------------
    # Screen update
    #---------------------------------------------------
    #Last thing drawn goes on top
    screen.fill(("black"))
    screen.blit(player_sprite, player.topleft)
    player.clamp_ip(pygame.Rect(0, 80, WINDOW_WIDTH, WINDOW_HEIGHT - 80))
    pygame.display.update()
    #---------------------------------------------------
    # End of screen update
    #---------------------------------------------------


    
    #---------------------------------------------------
    # End of main loop
    #---------------------------------------------------
pygame.quit()