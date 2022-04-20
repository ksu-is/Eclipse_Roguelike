from typing import Tuple

class Entity:
    #Represents object and NPCs in the world. Items, enemies, the player...
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        # 4 inputs, x/y are coordinates, char = the entity sprite, color = the color of the entity sprite
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        
    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy
        