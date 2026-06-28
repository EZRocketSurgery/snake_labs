import pygame
from game_engine import game_board

# step 1 make the board
board = game_board.GameBoard(10, 10)
board.set_draw_area(0, 0, 500, 500)
#general setup

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("snake_labs_render_test")
#game setup
#---------------------------------------------------
# definition setup
#---------------------------------------------------
def test_render():
    pass
def draw_grid(game_board):
    BG = (19, 24, 34)
    GRID = (40, 48, 63)
    """
    spacing is in pixels and is based on the draw area of the board
    so I need #TODO:
    - make the grid fit the draw area
    - make the grid match the tiles
    - make the grid update when the draw area changes (separate function for this)
    
    """
    spacing = None #TODO
    """Draw a simple background grid so movement is easy to observe."""
    for x in range(0, game_board.width, spacing):
        pygame.draw.line(screen, GRID, (x, 0), (x, game_board.height), 1)
    for y in range(0, game_board.height, spacing):
        pygame.draw.line(screen, GRID, (0, y), (game_board.width, y), 1)
#---------------------------------------------------
running = True
while running:
    clock = pygame.time.Clock().tick(60)  # Delta time in seconds
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #---------------------------------------------------
    screen.fill(("black"))
    #---------------------------------------------------
    # render test goes here
    #---------------------------------------------------
    test_render()


    # ---------------------------------------------------   
    pygame.display.update()