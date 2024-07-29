import tkinter as tk
from tkinter import Toplevel
import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    if (player == 'rock' and computer == 'scissors') or \
       (player == 'paper' and computer == 'rock') or \
       (player == 'scissors' and computer == 'paper'):
        return "You win!"
    return "You lose!"

def show_result(player, computer, result):
    result_window = Toplevel()
    result_window.title("Result")
    
    result_label = tk.Label(result_window, text=f"Computer chose: {computer}\n{result}", padx=20, pady=20)
    result_label.pack()
    
    close_button = tk.Button(result_window, text="Close", command=result_window.destroy)
    close_button.pack(pady=10)

def on_choice(choice):
    computer_choice = get_computer_choice()
    result = determine_winner(choice, computer_choice)
    show_result(choice, computer_choice, result)

app = tk.Tk()
app.title("Rock, Paper, Scissors")

tk.Label(app, text="Choose Rock, Paper, or Scissors:", padx=20, pady=20).pack()

tk.Button(app, text="Rock", command=lambda: on_choice('rock')).pack(side=tk.LEFT, padx=10)
tk.Button(app, text="Paper", command=lambda: on_choice('paper')).pack(side=tk.LEFT, padx=10)
tk.Button(app, text="Scissors", command=lambda: on_choice('scissors')).pack(side=tk.LEFT, padx=10)

app.mainloop()
