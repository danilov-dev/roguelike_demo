from models.hero import Hero
from models.game_field import GameField

class Game:
    def __init__(self):
        self.field: GameField | None = None
        self.hero: Hero | None = None
        self.current_room_index = 0
        self.items_collected = 0
        self.message = "Welcome! Use arrow keys to move."

    def start_new_game(self, size: int = 15, num_rooms: int = 3):
        self.field = GameField()
        self.field.create_field(size, num_rooms)

        self.hero = Hero()
        # Place hero at entrance of first room
        enter = self.field.rooms[0].enter
        self.hero.x = enter['x']
        self.hero.y = enter['y']
        self.message = f"Room 1/{num_rooms} - Find the exit (E)!"

    @property
    def current_room(self):
        if not self.field or not self.field.rooms:
            return None
        return self.field.rooms[self.current_room_index]

    @property
    def total_rooms(self):
        if not self.field:
            return 0
        return len(self.field.rooms)

    def can_move_to(self, x: int, y: int) -> bool:
        room = self.current_room
        if not room:
            return False
        size = len(room.field)
        if not (0 <= x < size and 0 <= y < size):
            return False
        cell = room.field[y][x]
        # Can walk on floor, start, exit, door, item
        return cell in [' ', '.', 'S', 'E', '+', '*']

    def move_hero(self, dx: int, dy: int) -> bool:
        if not self.hero or not self.current_room:
            return False

        new_x = self.hero.x + dx
        new_y = self.hero.y + dy

        if not self.can_move_to(new_x, new_y):
            self.message = "Blocked!"
            return False

        # Move hero
        self.hero.go(new_x, new_y)

        # Check what's at the new position
        room = self.current_room
        cell = room.field[new_y][new_x]

        # Collect item
        if cell == '*':
            room.field[new_y][new_x] = '.'  # Replace with floor
            self.items_collected += 1
            self.message = f"Item collected! Total: {self.items_collected}"

        # Check for exit
        elif cell == 'E':
            self._try_next_room()

        # Normal movement
        else:
            self.message = f"Room {self.current_room_index + 1}/{self.total_rooms}"

        return True

    def _try_next_room(self):
        """Try to move to the next room"""
        if self.current_room_index < self.total_rooms - 1:
            self.current_room_index += 1
            next_room = self.current_room
            # Place hero at entrance of next room
            self.hero.x = next_room.enter['x']
            self.hero.y = next_room.enter['y']
            self.message = f"Entered room {self.current_room_index + 1}/{self.total_rooms}!"
        else:
            self.message = "Congratulations! You've completed all rooms!"