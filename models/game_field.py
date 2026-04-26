import random
from models.room import Room
from models.tiles import Wall, Floor, Start, Exit, Item, Door

class GameField:
    def __init__(self):
        self.size = 0
        self.rooms: list[Room] = []

    def _generate_passage(self, size: int) -> dict:
        """Generate entrance/exit position on the room border"""
        pos_x = random.randint(0, size - 1)
        if pos_x == 0 or pos_x == size - 1:
            pos_y = random.randint(0, size - 1)
        else:
            pos_y = random.choice([0, size - 1])
        return {'x': pos_x, 'y': pos_y}

    def _create_room(self, size: int, room_num: int, total_rooms: int) -> Room:
        """Create a single room with walls, floor, entrance, exit and items"""
        field = [["#" for _ in range(size)] for _ in range(size)]

        # Generate entrance and exit
        enter_coord = self._generate_passage(size)
        exit_coord = self._generate_passage(size)

        while enter_coord == exit_coord:
            exit_coord = self._generate_passage(size)

        # Fill interior with floor
        for r in range(1, size - 1):
            for c in range(1, size - 1):
                if random.random() > 0.15:  # 85% chance of floor
                    field[r][c] = '.'
                else:
                    field[r][c] = ' '  # empty space variant

        # Set entrance and exit
        field[enter_coord['y']][enter_coord['x']] = 'S'
        field[exit_coord['y']][exit_coord['x']] = 'E'

        # Add some items (treasures)
        num_items = random.randint(2, 5)
        for _ in range(num_items):
            ix = random.randint(1, size - 2)
            iy = random.randint(1, size - 2)
            if field[iy][ix] in ['.', ' ']:
                field[iy][ix] = '*'

        # Add some doors (decorative for now)
        if random.random() > 0.5:
            dx = random.randint(1, size - 2)
            dy = random.randint(1, size - 2)
            if field[dy][dx] in ['.', ' ']:
                field[dy][dx] = '+'

        return Room(field=field, enter=enter_coord, exit=exit_coord)

    def _connect_rooms(self, room1: Room, room2: Room, size: int):
        """Create a corridor between two rooms (simplified - just marks exits)"""
        pass

    def create_field(self, size: int = 15, num_rooms: int = 3):
        """Generate multiple rooms"""
        self.size = size
        self.rooms = []

        for i in range(num_rooms):
            room = self._create_room(size, i, num_rooms)
            self.rooms.append(room)

        # Connect rooms (simplified)
        for i in range(len(self.rooms) - 1):
            self._connect_rooms(self.rooms[i], self.rooms[i + 1], size)