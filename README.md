# Tic Tac Toe Game
This is a classic Tic Tac Toe game implemented using Python and the Tkinter GUI library. Players take turns marking squares on a 3x3 grid, aiming to get three of their symbols (X or O) in a row, column, or diagonal. The first player to achieve this wins!

## Installation

1. **Prerequisites:** Ensure you have Python (version 3.x recommended) installed on your system. You can download it from https://www.python.org/downloads/.

2. **Install Libraries:** Open a terminal or command prompt and navigate to your project directory. Then, run the following command to install the required libraries:

```
pip install tkinter
```
## Running the Game

### Cloning the Repository

1. **Git Installation:** Ensure you have Git installed on your system. You can download it from https://www.git-scm.com/downloads.

2. **Open Terminal/Command Prompt:** Open a terminal or command prompt and navigate to the directory where you want to clone the Tic Tac Toe game repository.

3. **Clone Command:** Assuming the repository URL is https://github.com/username/tic-tac-toe (replace username with the actual username and tic-tac-toe with the repository name), execute the following command:

```
    git clone https://github.com/username/tic-tac-toe
```

This will clone the Tic Tac Toe game repository from GitHub into your specified directory. The downloaded files will be saved within a folder named tic-tac-toe (or the repository name, if different).

**Alternative: Manual Download**

If you don't have Git or prefer a manual approach:

1. **Access the Repository:** Visit the repository URL on GitHub.
2. **Download Files:** Click on the "Code" button and then the "Download ZIP" button. This will download a ZIP file containing the code.
3. **Extract Files:** Extract the downloaded ZIP file into your desired project directory. This will create a folder containing the game files.


### Execute the Script: In your terminal, navigate to the directory containing the files and run:
``` python3 layout.py```

**This will launch the Tic Tac Toe game window.**

## Gameplay Instructions

* Click on any empty square on the grid to place your mark (X or O).
* The game automatically switches between players after each move.
* If a player achieves three consecutive marks, a victory message will appear, and the game will reset.
* If all squares are filled without a winner, a "Tie!" message will display, and the game will reset.
* Use the "Reset" button to clear the board and start a new game anytime.
  
## Code Breakdown
* layout.py: This file handles the graphical user interface (GUI) using Tkinter and interacts with the logic defined in logic.py.
     * Creates the main window, buttons for the Tic Tac Toe grid, and a "Reset" button.
     * Defines functions to handle button clicks:
       * button_click_handler: Receives the button index and calls the logic.button_click function with this information.
        * reset_game_handler: Resets the game by clearing button text and calling logic.reset_game.

* logic.py: Contains the core game logic.

    * Manages game state variables like the current player and board representation.
    * Implements functions:
        * check_winner: Checks for a winning combination by iterating through possible rows, columns, and diagonals.
        * reset_game: Resets the game state (board and current player).
        * button_click: Handles a button click event:
            * Updates the corresponding board position with the current player's mark.
            * Disables the clicked button.
            * Checks for a winner or a tie using check_winner.
            * Displays a victory or tie message and resets the game if necessary.
            * Switches the current player.
## Customization

This Tic Tac Toe game provides a solid foundation. Here are some potential enhancements:
* Visual Theme: Modify the game's appearance by changing button colors, font styles, or adding background images using Tkinter's customization options.
* Difficulty Levels: Introduce opponents with varying difficulty levels to challenge players.
* Multiplayer Mode: Allow two players to compete locally on the same device. This would require tracking turns and disabling input for the non-active player.

## Further Exploration

For in-depth understanding of Tkinter and GUI development:
* **Tkinter Documentation:** https://docs.python.org/3/library/tk.html
* **Tutorials and Examples:** Numerous online resources offer Tkinter tutorials and example projects to explore further.

I trust this improved README provides a clear and informative guide for your Tic Tac Toe game!



