# Tic-Tac-Toe Game

## Overview

This project is a simple implementation of the Tic-Tac-Toe game using Python and the Pygame library. The game allows a player to compete against an AI with two different difficulty levels or play against another player in a local PvP mode. The AI employs a Minimax algorithm for optimal play or can choose moves randomly.

**Credits**: This project was guided by the Coding Spot YouTube channel.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/tic-tac-toe.git
   cd tic-tac-toe
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. Install the required Python packages:
   ```bash
   pip install pygame numpy
   ```

3. **Setup**:
   - Make sure you have the `constants.py` file in the same directory as the main script. This file should define constants such as `WIDTH`, `HEIGHT`, `ROWS`, `COLS`, `SQSIZE`, `LINE_WIDTH`, `LINE_COLOR`, `BG_COLOR`, `CROSS_COLOR`, `CIRC_COLOR`, `RADIUS`, and `CROSS_WIDTH`.

## Usage

1. **Run the Game**:
   ```bash
   python main.py
   ```

2. **Gameplay**:
   - **Player vs AI**: Click on the grid to make a move. The AI will take its turn automatically.
   - **Player vs Player**: Click on the grid to make a move. The second player will be prompted to make a move when it's their turn.

3. **Controls**:
   - **G**: Toggle between Player vs Player and Player vs AI modes.
   - **R**: Reset the game.
   - **0**: Set AI difficulty to random moves.
   - **1**: Set AI difficulty to Minimax algorithm.

4. **Exit**: Close the game window or press `Ctrl+C` in the terminal.

## Code Structure

### `constants.py`

This file should define all constants used in the game, such as board size, colors, and line widths.

### `Board` Class

- **`__init__`**: Initializes the board with empty squares.
- **`final_state`**: Checks for a win condition or a draw.
- **`mark_sqr`**: Marks a square with a player's move.
- **`empty_sqr`**: Checks if a square is empty.
- **`get_empty_sqrs`**: Returns a list of empty squares.
- **`isfull`**: Checks if the board is full.
- **`isempty`**: Checks if the board is empty.

### `AI` Class

- **`__init__`**: Initializes the AI with a difficulty level and player number.
- **`rnd`**: Chooses a random move.
- **`minimax`**: Implements the Minimax algorithm to find the best move.
- **`eval`**: Evaluates the best move based on the current difficulty level.

### `Game` Class

- **`__init__`**: Initializes the game state.
- **`make_move`**: Updates the board and switches the turn.
- **`show_lines`**: Draws the grid lines on the board.
- **`draw_fig`**: Draws X or O on the board.
- **`next_turn`**: Switches the active player.
- **`change_gamemode`**: Toggles between PvP and AI modes.
- **`isover`**: Checks if the game is over.
- **`reset`**: Resets the game state.

### `main`

The main game loop handles user input, AI moves, and updates the display. It manages game events such as mouse clicks and key presses.

## Contributing

Feel free to fork the repository and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Coding Spot YouTube Channel for the guided project tutorial.