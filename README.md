<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README</title>
</head>
<body>
    <h1>Tic-Tac-Toe Game</h1>

    <h2>Overview</h2>
    <p>
        This project is a simple implementation of the Tic-Tac-Toe game using Python and the Pygame library. The game allows a player to compete against an AI with two different difficulty levels or play against another player in a local PvP mode. The AI employs a Minimax algorithm for optimal play or can choose moves randomly.
    </p>
    <p><strong>Credits</strong>: This project was guided by the Coding Spot YouTube channel.</p>

    <h2>Installation</h2>
    <ol>
        <li><strong>Clone the Repository</strong>:
            <pre><code>git clone https://github.com/yourusername/tic-tac-toe.git
cd tic-tac-toe</code></pre>
        </li>
        <li><strong>Install Dependencies</strong>:
            <pre><code>pip install pygame numpy</code></pre>
        </li>
        <li><strong>Setup</strong>:
            <p>Make sure you have the <code>constants.py</code> file in the same directory as the main script. This file should define constants such as <code>WIDTH</code>, <code>HEIGHT</code>, <code>ROWS</code>, <code>COLS</code>, <code>SQSIZE</code>, <code>LINE_WIDTH</code>, <code>LINE_COLOR</code>, <code>BG_COLOR</code>, <code>CROSS_COLOR</code>, <code>CIRC_COLOR</code>, <code>RADIUS</code>, and <code>CROSS_WIDTH</code>.</p>
        </li>
    </ol>

    <h2>Usage</h2>
    <ol>
        <li><strong>Run the Game</strong>:
            <pre><code>python main.py</code></pre>
        </li>
        <li><strong>Gameplay</strong>:
            <ul>
                <li><strong>Player vs AI</strong>: Click on the grid to make a move. The AI will take its turn automatically.</li>
                <li><strong>Player vs Player</strong>: Click on the grid to make a move. The second player will be prompted to make a move when it's their turn.</li>
            </ul>
        </li>
        <li><strong>Controls</strong>:
            <ul>
                <li><strong>G</strong>: Toggle between Player vs Player and Player vs AI modes.</li>
                <li><strong>R</strong>: Reset the game.</li>
                <li><strong>0</strong>: Set AI difficulty to random moves.</li>
                <li><strong>1</strong>: Set AI difficulty to Minimax algorithm.</li>
            </ul>
        </li>
        <li><strong>Exit</strong>: Close the game window or press <code>Ctrl+C</code> in the terminal.</li>
    </ol>

    <h2>Code Structure</h2>
    <h3><code>constants.py</code></h3>
    <p>This file should define all constants used in the game, such as board size, colors, and line widths.</p>

    <h3><code>Board</code> Class</h3>
    <ul>
        <li><code>__init__</code>: Initializes the board with empty squares.</li>
        <li><code>final_state</code>: Checks for a win condition or a draw.</li>
        <li><code>mark_sqr</code>: Marks a square with a player's move.</li>
        <li><code>empty_sqr</code>: Checks if a square is empty.</li>
        <li><code>get_empty_sqrs</code>: Returns a list of empty squares.</li>
        <li><code>isfull</code>: Checks if the board is full.</li>
        <li><code>isempty</code>: Checks if the board is empty.</li>
    </ul>

    <h3><code>AI</code> Class</h3>
    <ul>
        <li><code>__init__</code>: Initializes the AI with a difficulty level and player number.</li>
        <li><code>rnd</code>: Chooses a random move.</li>
        <li><code>minimax</code>: Implements the Minimax algorithm to find the best move.</li>
        <li><code>eval</code>: Evaluates the best move based on the current difficulty level.</li>
    </ul>

    <h3><code>Game</code> Class</h3>
    <ul>
        <li><code>__init__</code>: Initializes the game state.</li>
        <li><code>make_move</code>: Updates the board and switches the turn.</li>
        <li><code>show_lines</code>: Draws the grid lines on the board.</li>
        <li><code>draw_fig</code>: Draws X or O on the board.</li>
        <li><code>next_turn</code>: Switches the active player.</li>
        <li><code>change_gamemode</code>: Toggles between PvP and AI modes.</li>
        <li><code>isover</code>: Checks if the game is over.</li>
        <li><code>reset</code>: Resets the game state.</li>
    </ul>

    <h3><code>main</code></h3>
    <p>The main game loop handles user input, AI moves, and updates the display. It manages game events such as mouse clicks and key presses.</p>

    <h2>Contributing</h2>
    <p>Feel free to fork the repository and submit pull requests. Contributions are welcome!</p>

    <h2>License</h2>
    <p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>

    <h2>Acknowledgements</h2>
    <p>Coding Spot YouTube Channel for the guided project tutorial.</p>
</body>
</html>
