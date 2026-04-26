from models.game import Game
from core.renderer import Renderer

def main():
    game = Game()
    game.start_new_game(size=15, num_rooms=3)

    renderer = Renderer(cell_size=30)
    renderer.render(game)
    renderer.bind_keys(game)
    renderer.show()

if __name__ == "__main__":
    main()