# Roguelike Game - Portfolio Demo

[🇬🇧 English Version](README_EN.md) | [🇷🇺 Русская версия](README_RU.md)

A simple roguelike game built with Python and Tkinter, demonstrating core game development concepts.

## Features

- **Procedural Room Generation**: Multiple rooms are randomly generated with walls, floors, and passages
- **Hero Movement**: Arrow keys or WASD to move the hero around
- **Collision Detection**: Walls block movement, floors and items are passable
- **Item Collection**: Collect golden items (*) scattered throughout rooms
- **Room Transitions**: Reach the exit (E) to advance to the next room
- **Visual Feedback**: Real-time display of messages, item count, and current room

## Controls

| Key | Action |
|-----|--------|
| ↑ / W | Move Up |
| ↓ / S | Move Down |
| ← / A | Move Left |
| → / D | Move Right |
| R | Restart Game |

## Tile Legend

| Symbol | Name | Description |
|--------|------|-------------|
| # | Wall | Impassable barrier |
| . | Floor | Walkable surface |
| S | Start | Starting position (green) |
| E | Exit | Exit to next room (orange) |
| * | Item | Collectible treasure (gold) |
| + | Door | Decorative door |
| ● | Hero | Player character (green circle) |

## Project Structure

```
/workspace
├── main.py              # Entry point
├── models/
│   ├── game.py          # Main game logic
│   ├── game_field.py    # Room generation
│   ├── hero.py          # Hero class
│   ├── room.py          # Room data structure
│   └── tiles.py         # Tile types and colors
└── core/
    └── renderer.py      # Tkinter-based rendering
```

## Running the Game

```bash
python main.py
```

**Requirements**: Python 3.8+, Tkinter (usually included with Python)

## Code Architecture Highlights

### Object-Oriented Design
- **Hero**: Manages player position and movement
- **Room**: Contains field data and entrance/exit points
- **GameField**: Handles procedural generation of multiple rooms
- **Game**: Core game logic including collision detection and state management
- **Renderer**: Separates rendering logic from game logic

### Key Concepts Demonstrated
1. **Procedural Generation**: Random room layouts with guaranteed paths
2. **Tile-Based Rendering**: Grid-based map system
3. **Collision Detection**: Check tile properties before movement
4. **State Management**: Track items, rooms, and game progress
5. **Event-Driven Input**: Keyboard handling for real-time controls

## Future Enhancements

Potential features for portfolio expansion:
- Enemy AI and combat system
- Inventory management
- Multiple levels with increasing difficulty
- Save/Load functionality
- Sound effects and music
- Enhanced graphics with sprites

## License

Demo code for portfolio purposes.