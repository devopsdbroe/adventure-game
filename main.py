import tkinter as tk
from game_gui import GameGUI

def main():
    root = tk.Tk()
    app = GameGUI(root)
    app.setup_gui()
    root.mainloop()

if __name__ == "__main__":
    main()