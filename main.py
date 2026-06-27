import pygame

#general setup
pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720


screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("snake_labs")

#game setup

running = True
while running:
#---------------------------------------------------
# Timekeeping
#---------------------------------------------------

    clock = pygame.time.Clock().tick(60)  # Delta time in seconds

#---------------------------------------------------
# Event handling
#---------------------------------------------------

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#---------------------------------------------------
# End of event handling
#---------------------------------------------------
    #indent holder
#---------------------------------------------------
# Screen update
#---------------------------------------------------

    #Last thing drawn goes on top
    screen.fill(("black"))
    pygame.display.update()

#---------------------------------------------------
# End of screen update
#---------------------------------------------------
    #indent holder
#---------------------------------------------------
# End of main loop
#---------------------------------------------------
pygame.quit()