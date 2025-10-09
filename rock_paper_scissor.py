import tkinter as tk
from tkinter import Label, PhotoImage
from PIL import Image, ImageTk
import random
user_score = 0
computer_score = 0

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)
    
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1
    
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("600x400")
root.resizable(False, False)

image = Image.open("rps_bg.png")
image = image.resize((600, 400))
background_image = ImageTk.PhotoImage(image)

background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16), bg="black").pack(pady=10)
result_label = tk.Label(root, text="Choose an option:", font=("Arial", 12), bg="black")
result_label.pack(pady=10)
score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12), bg="black")
score_label.pack(pady=10)

tk.Button(root, text="Rock", command=lambda: play("Rock"), width=50).pack(pady=5)
tk.Button(root, text="Paper", command=lambda: play("Paper"), width=50).pack(pady=5)
tk.Button(root, text="Scissors", command=lambda: play("Scissors"), width=50).pack(pady=5)

root.mainloop()