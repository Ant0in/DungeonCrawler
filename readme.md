# 🌀 Dungeon Crawler

Welcome to **DungeonCrawler**! This project is an interactive maze game where you navigate through a randomly generated labyrinth to find the exit. 🧩

## 🚀 Features

- **Random Maze Generation**: Every game is unique thanks to a recursive generation algorithm.
- **Interactive Movement**: Use arrow keys to explore the maze.
- **Limited Vision**: The player can only see tiles near their position.
- **Hidden Exit**: Find the exit to win the game!

## 🕹️ Controls

- **Arrow Keys**: Move the player in the maze.
- **Escape**: Quit the game.

## 📦 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Ant0in/DungeonCrawler
   cd DungeonCrawler
   ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the game:

    ```bash
    python src/main.py
    ```

## ⚙️ Arguments

You can customize the maze size and other parameters using the following arguments:

- `--width`: Maze width (default: `20`).
- `--height`: Maze height (default: `10`).
- `--player_pos`: Initial player position (default: `0,0`).
- `--player_vision`: Player's vision radius (default: `5`).

**Example**:

```python
python main.py --width 15 --height 15 --player_pos 1,1 --player_vision 3
```

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
