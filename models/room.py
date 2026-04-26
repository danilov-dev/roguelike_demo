class Room:
    def __init__(self, field: list[list[str]], enter: dict[str, int], exit: dict[str, int]):
        self.field = field
        self.enter = enter
        self.exit = exit
