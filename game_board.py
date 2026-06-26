class GameBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    def get_tile(self, x, y):
        tile = None
        return tile #TODO: implement tile retrieval

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = []
        self.contents = None #placeholder for holding stuff