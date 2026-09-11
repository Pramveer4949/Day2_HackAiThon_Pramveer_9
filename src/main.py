import tkinter as tk
import random


# -----------------------------
# GAME VARIABLES
# -----------------------------

k = random.randint(1, 50)
attempts = 0
max_attempts = 5


# -----------------------------
# FUNCTIONS
# -----------------------------

def check_guess():
    global attempts

    try:
        guess = int(guess_entry.get())
    except ValueError:
        message_label.config(
            text="Please enter a number!",
            fg="orange"
        )
        return

    if guess < 1 or guess > 50:
        message_label.config(
            text="Enter a number between 1 and 50!",
            fg="orange"
        )
        return

    attempts += 1

    attempts_label.config(
        text=f"Attempts: {attempts}/{max_attempts}"
    )

    if guess == k:
        message_label.config(
            text="🎉 Congratulations! You guessed the number!",
            fg="#00ff88"
        )

        guess_button.config(state="disabled")

    elif guess > k:
        message_label.config(
            text="⬇ Think Lower!",
            fg="#ffcc00"
        )

    else:
        message_label.config(
            text="⬆ Think Higher!",
            fg="#00ccff"
        )

    if attempts >= max_attempts and guess != k:
        message_label.config(
            text=f"😢 Game Over! The number was {k}",
            fg="#ff5555"
        )

        guess_button.config(state="disabled")


def restart_game():
    global k, attempts

    k = random.randint(1, 50)
    attempts = 0

    attempts_label.config(
        text="Attempts: 0/5"
    )

    message_label.config(
        text="Make your first guess!",
        fg="white"
    )

    guess_entry.delete(0, tk.END)

    guess_button.config(state="normal")


# -----------------------------
# MAIN WINDOW
# -----------------------------

root = tk.Tk()

root.title("Number Guessing Game")
root.geometry("600x500")
root.resizable(False, False)

root.configure(bg="#101820")


# -----------------------------
# TITLE
# -----------------------------

title_label = tk.Label(
    root,
    text="🎯 NUMBER GUESSING GAME",
    font=("Arial", 28, "bold"),
    fg="#00ffcc",
    bg="#101820"
)

title_label.pack(pady=40)


# -----------------------------
# INSTRUCTIONS
# -----------------------------

instruction_label = tk.Label(
    root,
    text="Guess a number between 1 and 50",
    font=("Arial", 16),
    fg="white",
    bg="#101820"
)

instruction_label.pack(pady=10)


# -----------------------------
# INPUT BOX
# -----------------------------

guess_entry = tk.Entry(
    root,
    font=("Arial", 22),
    justify="center",
    width=10
)

guess_entry.pack(pady=20)


# -----------------------------
# GUESS BUTTON
# -----------------------------

guess_button = tk.Button(
    root,
    text="GUESS",
    font=("Arial", 16, "bold"),
    bg="#00cc99",
    fg="white",
    activebackground="#00aa80",
    width=15,
    command=check_guess
)

guess_button.pack(pady=10)


# -----------------------------
# ATTEMPTS
# -----------------------------

attempts_label = tk.Label(
    root,
    text="Attempts: 0/5",
    font=("Arial", 15, "bold"),
    fg="#cccccc",
    bg="#101820"
)

attempts_label.pack(pady=15)


# -----------------------------
# MESSAGE
# -----------------------------

message_label = tk.Label(
    root,
    text="Make your first guess!",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#101820"
)

message_label.pack(pady=15)


# -----------------------------
# RESTART BUTTON
# -----------------------------

restart_button = tk.Button(
    root,
    text="PLAY AGAIN",
    font=("Arial", 14, "bold"),
    bg="#4444aa",
    fg="white",
    width=15,
    command=restart_game
)

restart_button.pack(pady=20)


# -----------------------------
# START GUI
# -----------------------------

root.mainloop()

    
    
