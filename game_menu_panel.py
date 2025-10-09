import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import sys
import os
import platform

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def launch_game(script_name):
    if platform.system() == 'Windows':
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        subprocess.Popen([sys.executable, os.path.join(BASE_DIR, script_name)], startupinfo=startupinfo)
    else:
        subprocess.Popen([sys.executable, os.path.join(BASE_DIR, script_name)])
def launch_pong():
    launch_game("pingpong.py") 
def launch_rps():
    launch_game("rock_paper_scissor.py")
def launch_tictactoe():
    launch_game("tictactoe.py")
def launch_flappybird():
    launch_game("Bouncy_Ball.py")
def load_resized_image(filename, width, height):
    path = os.path.join(BASE_DIR, filename)
    img = Image.open(path)
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)
root = tk.Tk()
root.title("Mini Game Arcade")
root.attributes('-fullscreen', True)
root.configure(bg="#000000")
main_frame = tk.Frame(root, bg="#000000")
main_frame.pack(fill="both", expand=True, padx=20, pady=20)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
grid_width = (screen_width - 40) // 2
grid_height = (screen_height - 40) // 2
games = [
    ("Space Ball", "images/pong.png", launch_pong),
    ("Rock Paper Scissors", "images/rps.png", launch_rps),
    ("Tic Tac Toe", "images/ttt.png", launch_tictactoe),
    ("Bouncy Ball", "images/bouncy.png", launch_flappybird)
]
game_images = []
for name, img_file, _ in games:
    game_images.append(load_resized_image(img_file, grid_width-40, grid_height-100))
for i, (name, _, command) in enumerate(games):
    container = tk.Frame(main_frame, bg="#000000")
    container.grid(row=i//2, column=i%2, padx=10, pady=10, sticky="nsew")
    container.grid_propagate(False)
    
    frame = tk.Frame(container, bg="#000000", bd=2, relief="raised")
    frame.pack(fill="both", expand=True)
    
    img_frame = tk.Frame(frame, bg="#000000")
    img_frame.pack(fill="both", expand=True, pady=(0, 0))
    img_label = tk.Label(img_frame, image=game_images[i], bg="#000000")
    img_label.image = game_images[i]
    img_label.pack(fill="both", expand=True)
    title_frame = tk.Frame(frame, bg="#000000", height=40)
    title_frame.pack(fill="x", side="bottom", pady=(0, 0))
    title = tk.Label(title_frame, text=name, font=("Arial", 18, "bold"), 
                   bg="#000000", fg="#FFFFFF", padx=10, pady=5)
    title.pack(fill="x", expand=True)
    def make_callback(cmd=command):
        return lambda e: cmd()
    for widget in [frame, img_label, title_frame, title]:
        widget.bind("<Button-1>", make_callback())
for i in range(2):
    main_frame.columnconfigure(i, weight=1, uniform="cols")
for i in range(2):
    main_frame.rowconfigure(i, weight=1, uniform="rows")
def toggle_fullscreen(event=None):
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))
root.bind('<Escape>', toggle_fullscreen)

root.mainloop()