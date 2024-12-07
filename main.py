import tkinter as tk
from game import Game
from name_prompt import NamePrompt
from player import Player
from computer import Computer
from gesture import Gesture

def main():
    """
    Sanya Gupta
    CMSY 257
    Starts the GUI loop and instantiates necessary objects
    """
    root = tk.Tk()
    name_prompt = NamePrompt(root)
    root.mainloop()  # Run the event loop until a name is submitted

    player_name = name_prompt.get_name()
    if not player_name:
        print("No name entered. Exiting game.")
        return
    
    # Initialize game components
    player = Player(player_name, "")
    computer = Computer()
    gesture = Gesture()

    # Pass the root and other objects to the Game class
    game = Game(root, player, computer, gesture, rounds=3)
    game.start()

    root.mainloop()

if __name__ == "__main__":
    main()
