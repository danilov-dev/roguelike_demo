import tkinter as tk
from models.game import Game

class Renderer:
    def __init__(self, cell_size: int = 30):
        self.cell_size = cell_size
        self.root = tk.Tk()
        self.root.title("Roguelike - Portfolio Demo")
        self.canvas = None
        self.info_label = None

    def render(self, game: Game):
        room = game.current_room
        if not room:
            return

        field = room.field
        size = len(field)

        # Create canvas if needed
        canvas_size = size * self.cell_size
        if self.canvas is None:
            self.canvas = tk.Canvas(self.root, width=canvas_size, height=canvas_size, bg='#2b2b2b')
            self.canvas.pack(pady=10)

            # Info label for messages and stats
            self.info_label = tk.Label(
                self.root,
                text="",
                font=('Arial', 12),
                bg='#f0f0f0',
                padx=10,
                pady=5
            )
            self.info_label.pack()
        else:
            self.canvas.delete("all")

        # Draw tiles
        for y in range(size):
            for x in range(size):
                char = field[y][x]
                color = self._get_tile_color(char)
                x1, y1 = x * self.cell_size, y * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size

                # Draw tile background
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#3a3a3a", width=1)

                # Draw symbol for items/doors
                if char in ['*', '+', 'S', 'E']:
                    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                    self.canvas.create_text(
                        cx, cy,
                        text=char,
                        font=('Arial', self.cell_size // 2, 'bold'),
                        fill='black' if char in ['S', 'E'] else 'white'
                    )

        # Draw hero
        if game.hero:
            hx, hy = game.hero.x, game.hero.y
            x1 = hx * self.cell_size + 5
            y1 = hy * self.cell_size + 5
            x2 = (hx + 1) * self.cell_size - 5
            y2 = (hy + 1) * self.cell_size - 5
            self.canvas.create_oval(x1, y1, x2, y2, fill="#2e8b57", outline="navy", width=2)

        # Update info label
        if self.info_label:
            info_text = f"{game.message} | Items: {game.items_collected} | Room: {game.current_room_index + 1}/{game.total_rooms}"
            self.info_label.config(text=info_text)

    def _get_tile_color(self, char: str) -> str:
        """Get color for each tile type"""
        colors = {
            '#': "#4a4a4a",  # Wall - dark gray
            '.': "#c7c7c7",  # Floor - light gray
            ' ': "#d4d4d4",  # Empty floor variant
            '+': "#cd8162",  # Door - brown/orange
            'S': "#90EE90",  # Start - light green
            'E': "#FFA500",  # Exit - orange
            '*': "#FFD700",  # Item - gold
        }
        return colors.get(char, "#808080")

    def bind_keys(self, game: Game):
        def on_key(event):
            key = event.keysym
            moved = False

            if key == "Up" or key == "w":
                moved = game.move_hero(0, -1)
            elif key == "Down" or key == "s":
                moved = game.move_hero(0, 1)
            elif key == "Left" or key == "a":
                moved = game.move_hero(-1, 0)
            elif key == "Right" or key == "d":
                moved = game.move_hero(1, 0)
            elif key == "r" or key == "R":
                # Restart game
                game.start_new_game(size=15, num_rooms=3)
                moved = True

            if moved:
                self.render(game)

        self.root.bind("<Key>", on_key)
        if self.canvas:
            self.canvas.focus_set()

    def show(self):
        self.root.mainloop()