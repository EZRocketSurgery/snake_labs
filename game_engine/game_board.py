class GameBoard:
    """Represents a 2D grid of tiles for the game world."""
    def __init__(self, width, height, draw_area=None):
        self.width = width
        self.height = height
        self.area = width * height
        self.grid = []
        self.draw_area = draw_area if draw_area else (0, 0, 0, 0)
        """
        draw_area is a tuple of (left_edge, top_edge, pixel_width, pixel_height) 
        following the pygame convention for rects.
        """
        for y in range(height):
            row = []
            for x in range(width):
                row.append(Tile(x, y))
            self.grid.append(row)

    def get_tile(self, x:int, y:int):
        """Returns the tile at the specified coordinates, or None if out of bounds."""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        else:
            return None
    
    def set_draw_area(self, left_x, top_y, width, height):
        """Sets the area of the board that should be drawn on the screen."""
        self.draw_area = (left_x, top_y, width, height)

class Tile:
    """Represents a single tile on the game board."""
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
        self.skin = None #placeholder for tile skin
        self.neighbors = []
        self.contents = None #placeholder for holding stuff
