import tkinter as tk
from tkinter import Canvas
import time

root = tk.Tk()
root.title("Tic Tac Toe")
root.resizable(False, False)
root.configure(bg='white')

canvas = Canvas(root, width=600, height=600, bg="white", highlightthickness=0)
canvas.grid(row=0, column=0)

current_player = "X"
player_colors = {"X": "blue", "O": "red"}
board = [["" for _ in range(3)] for _ in range(3)]
scores = {"X": 0, "O": 0}
tied_rounds = 0
total_rounds = 3
current_round = 1
starting_player = "X"
game_active = True

def draw_grid():
    canvas.delete("grid")
    canvas.create_line(200, 0, 200, 600, width=4, fill="black", tags="grid")
    canvas.create_line(400, 0, 400, 600, width=4, fill="black", tags="grid")
    canvas.create_line(0, 200, 600, 200, width=4, fill="black", tags="grid")
    canvas.create_line(0, 400, 600, 400, width=4, fill="black", tags="grid")

def draw_symbol(row, col, symbol):
    x1, y1 = col * 200, row * 200
    x2, y2 = x1 + 200, y1 + 200
    center_x, center_y = x1 + 100, y1 + 100
    color = player_colors[symbol]

    if symbol == "X":
        offset = 50
        canvas.create_line(x1 + offset, y1 + offset, x2 - offset, y2 - offset, width=6, fill=color)
        canvas.create_line(x1 + offset, y2 - offset, x2 - offset, y1 + offset, width=6, fill=color)
    else:
        radius = 50
        canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, width=6, outline=color)

turn_text = canvas.create_text(300, 20, text="Player X's Turn", font=("Arial", 24), fill="black", tags="text", stipple="gray50")

def update_turn_text():
    canvas.itemconfig(turn_text, text=f"Player {current_player}'s Turn")

def end_game_animation(winner):
    canvas.delete("all")
    color = player_colors[winner]
    root.configure(bg=color)
    canvas.configure(bg=color)

    win_text = canvas.create_text(300, -50, text=f"Player {winner} Wins!", font=("Arial", 36, "bold"), fill="white")
    score_text = canvas.create_text(300, 650, text=f"Final Score - X: {scores['X']} | O: {scores['O']}", font=("Arial", 20), fill="white")

    def animate():
        for i in range(50):
            canvas.move(win_text, 0, 2)
            canvas.move(score_text, 0, -2)
            canvas.update()
            time.sleep(0.02)

    root.after(100, animate)

def check_winner():
    for i in range(3):
        if board[i][0] != "" and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] != "" and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    if board[0][0] != "" and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != "" and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

def is_board_full():
    return all(cell != "" for row in board for cell in row)

def on_click(event):
    global current_player, board, current_round, total_rounds, tied_rounds, starting_player, game_active

    if not game_active:
        return

    col = event.x // 200
    row = event.y // 200

    if board[row][col] == "":
        board[row][col] = current_player
        draw_symbol(row, col, current_player)

        winner = check_winner()
        if winner:
            scores[winner] += 1
            canvas.itemconfig(turn_text, text=f"Player {winner} Wins Round {current_round}!", fill="black")
            game_active = False
            starting_player = "O" if winner == "X" else "X"
            if current_round == total_rounds:
                root.after(1500, lambda: end_game_animation(winner))
            else:
                root.after(1500, next_round)
        elif is_board_full():
            canvas.itemconfig(turn_text, text="Round Tied!", fill="black")
            tied_rounds += 1
            total_rounds += 1
            game_active = False
            root.after(1500, next_round)
        else:
            current_player = "O" if current_player == "X" else "X"
            update_turn_text()
        update_score_labels()

def next_round():
    global board, current_round, current_player, game_active

    if current_round >= total_rounds:
        winner = "X" if scores["X"] > scores["O"] else "O"
        end_game_animation(winner)
        return

    current_round += 1
    board = [["" for _ in range(3)] for _ in range(3)]
    canvas.delete("all")
    draw_grid()
    current_player = starting_player
    game_active = True
    update_turn_text()
    update_score_labels()

score_frame = tk.Frame(root, bg='white')
score_frame.grid(row=1, column=0, pady=10)

p1_label = tk.Label(score_frame, text="Player X (Blue): 0", font=("Arial", 14), bg='white', fg='black')
p1_label.grid(row=0, column=0, padx=20)
p2_label = tk.Label(score_frame, text="Player O (Red): 0", font=("Arial", 14), bg='white', fg='black')
p2_label.grid(row=0, column=1, padx=20)
round_label = tk.Label(score_frame, text=f"Round: {current_round} / {total_rounds}", font=("Arial", 14), bg='white', fg='black')
round_label.grid(row=1, column=0, columnspan=2)
tie_label = tk.Label(score_frame, text=f"Tied Rounds: {tied_rounds}", font=("Arial", 14), bg='white', fg='black')
tie_label.grid(row=2, column=0, columnspan=2)

def update_score_labels():
    p1_label.config(text=f"Player X (Blue): {scores['X']}")
    p2_label.config(text=f"Player O (Red): {scores['O']}")
    round_label.config(text=f"Round: {current_round} / {total_rounds}")
    tie_label.config(text=f"Tied Rounds: {tied_rounds}")

canvas.bind("<Button-1>", on_click)
draw_grid()
update_turn_text()

root.mainloop()