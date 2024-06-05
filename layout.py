from tkinter import *
import logic

# Initialize the main window
root = Tk()
root.title("Tic Tac Toe")
root.configure(bg="skyblue")
root.geometry("600x500")  # Increased window height to accommodate the reset button

mainframe = Frame(root, bg="skyblue")
mainframe.pack(expand=True)

# Create buttons and place them in the grid
buttons = []
for i in range(9):
    btn = Button(mainframe, text="", font=("times", 26, "bold"), height=3, width=6, bg="pink")
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Function to handle button click events (call logic.button_click)
def button_click_handler(index):
    logic.button_click(index, buttons[index])  # Pass button object

# Bind button click events
for i in range(9):
    buttons[i].config(command=lambda i=i: button_click_handler(i))

# Create a function to call reset_game from logic.py (implement reset button or logic)
def reset_game_handler():
    for btn in buttons:
        btn.config(text="")  # Clear button text
        btn.config(state="normal")  # Enable buttons
    logic.reset_game()

# Create a reset button
reset_button = Button(mainframe, text="Reset", font=("times", 16, "bold"), height=2, width=10, bg="lightgray", command=reset_game_handler)
reset_button.grid(row=3, columnspan=3, pady=20)  # Place the reset button a bit lower from the grid of Tic Tac Toe buttons

root.mainloop()
