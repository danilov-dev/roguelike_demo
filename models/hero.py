class Hero:
    def __init__(self):
        self.x = 0
        self.y = 0

    def go(self, new_x: int, new_y: int):
        self.x = new_x
        self.y = new_y