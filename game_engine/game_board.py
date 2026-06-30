import pygame


class GameBoard:
    """Represents a 2D grid of tiles for the game world."""
    def __init__(self, width: int, height: int, draw_area: tuple = None):
        self.width = width #in tiles
        self.height = height #in tiles
        self.area = width * height #in tiles
        self.grid_2d = [] #tiles in a 2D list: grid[y][x]
        self.grid = [] #tiles in a 1D list
        self.draw_area = draw_area if draw_area else (0, 0, 0, 0)
        """
        draw_area is a tuple of (left_x, top_y, pixel_width, pixel_height) 
        following the pygame convention for rects.
        """
        for y in range(height):
            row = []
            for x in range(width):
                tile = Tile(x, y)
                row.append(tile)
                self.grid.append(tile)
            self.grid_2d.append(row)

    def get_tile(self, x:int, y:int):
        """Returns the tile at the specified coordinates, or None if out of bounds."""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid_2d[y][x]
        else:
            return None
    
    def set_draw_area(self, left_x: float, top_y: float, width: float, height: float):
        """Sets the area of the board that should be drawn on the screen."""
        #TODO make some weird transformations to make moving tiles maybe?
        self.draw_area = (left_x, top_y, width, height)

    def draw_board(game_board: "GameBoard", screen: pygame.Surface, grid_color = (40, 48, 63), board_color = (30, 36, 50)):
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

    def do_to_all_tiles(self, func: callable):
        """Applies the given function to every tile on the board."""
        for tile in self.grid:
            func(tile)

class Tile:
    """Represents a single tile on the game board."""
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
        self.skin = None #placeholder for tile skin
        self.neighbors = []
        self.contents = None #placeholder for holding stuff

    def add_neighbor(self, neighbor_tile):
        """Adds a neighboring tile to this tile's list of neighbors."""
        self.neighbors.append(neighbor_tile)