"""
This file contains the base Entity class and any other classes that represent entities in the game world
such as the player, buildings, items, ect. The Entity class is meant to be a simple base class that
other classes can inherit from and expand upon. It should contain any common attributes or methods
that all entities will need, such as position, movement, inventory, ect.
The Entity class should not contain any level-specific logic or attributes
"""

class Entity:
    """Base class for all entities in the game."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Bot(Entity):
    """Represents a bot in the game world."""
    def __init__(self, x, y):
        super().__init__(x, y)
        self.inventory = [] #placeholder for inventory system