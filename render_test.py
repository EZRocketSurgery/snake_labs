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
BG_COLOR = (19, 24, 34)
def test_render():
    pass
def draw_board(game_board: game_board.GameBoard, grid_color=(40, 48, 63), board_color=(30, 36, 50)):
    """Draws the game board on the screen using pygame."""
    GRID_COLOR = grid_color
    BOARD_COLOR = board_color
    (left_x, top_y, pixel_width, pixel_height) = game_board.draw_area
    pygame.draw.rect(screen, BOARD_COLOR, (left_x, top_y, pixel_width, pixel_height))
    horizontal_spacing = (pixel_width/game_board.width)
    vertical_spacing = (pixel_height/game_board.height)
    for x in range(game_board.width + 1):
        pygame.draw.line(screen, GRID_COLOR, (left_x, top_y + vertical_spacing * x), (left_x + pixel_width, top_y + vertical_spacing * x), 1)
    for y in range(game_board.height + 1):
        pygame.draw.line(screen, GRID_COLOR, (left_x + horizontal_spacing * y, top_y), (left_x + horizontal_spacing * y, top_y + pixel_height), 1)

#---------------------------------------------------
running = True
clock = pygame.time.Clock()
left_x, top_y = 0, 0
while running:
    delta_time = clock.tick(60)/1000  # Delta time in milisecs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #---------------------------------------------------
    screen.fill(BG_COLOR)
    #---------------------------------------------------
    # render test goes here
    #---------------------------------------------------
    draw_board(board)
    if left_x < (WINDOW_WIDTH - 500):
        left_x += 1 
    if top_y < (WINDOW_HEIGHT - 500):
        top_y += 1
    board.set_draw_area(left_x, top_y, 500, 500)
    # ---------------------------------------------------   
    pygame.display.update()