from tkinter import messagebox

# Global variables for images and game state
current_player = "X"
board = ["", "", "", "", "", "", "", "", ""]

# Function to check for a winner or a tie
def check_winner():
    winner = None
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != "":
            winner = board[combo[0]]
    return winner

# Function to reset the game
def reset_game():
    global board, current_player
    board = ["", "", "", "", "", "", "", "", ""]
    current_player = "X"

# Function to handle button click
def button_click(index, button):
    global current_player
    if board[index] == "":
        if current_player == "X":
            button.config(text="X")
            board[index] = "X"
        else:
            button.config(text="O")
            board[index] = "O"
        current_player = "O" if current_player == "X" else "X"
        button.config(state="disabled")
        
        winner = check_winner()
        if winner:
            messagebox.showinfo("Winner!", f"{winner} wins!")
            reset_game()
        elif "" not in board:
            messagebox.showinfo("Tie!", "It's a tie!")
            reset_game()
