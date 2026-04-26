from abc import ABC

class Tile(ABC):
    passable: bool
    color: str
    symbol: str

class Floor(Tile):
    passable = True
    color = '#c7c7c7'
    symbol = '.'

class Wall(Tile):
    passable = False
    color = '#4a4a4a'
    symbol = '#'

class Door(Tile):
    passable = True
    color = '#cd8162'
    symbol = '+'

class Start(Tile):
    passable = True
    color = '#90EE90'
    symbol = 'S'

class Exit(Tile):
    passable = True
    color = '#FFA500'
    symbol = 'E'

class Item(Tile):
    passable = True
    color = '#FFD700'
    symbol = '*'

def get_tile(char: str) -> Tile:
    """Convert character to Tile instance"""
    tile_map = {
        '#': Wall,
        '.': Floor,
        ' ': Floor,
        '+': Door,
        'S': Start,
        'E': Exit,
        '*': Item,
    }
    tile_class = tile_map.get(char, Floor)
    return tile_class()