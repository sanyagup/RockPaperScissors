from computer import Computer
from gesture import Gesture
from player import Player
from round import Round
import tkinter as tk
from tkinter import messagebox

class Game:
    """
    Sanya Gupta
    Represents the Rock, Paper, Scissors game."""

    def __init__(self, root, player, computer, gesture, rounds=3):
        """Initialize the game with a player, a computer, and number of rounds."""
        self.rounds = rounds
        self.root = root
        self.player = player
        self.computer = computer
        self.current_round = 1
        self.gesture = gesture
        self.choice = tk.StringVar(value="yes")
        self.winner = ''

    def play_round(self):
        """
        Play a single round of the game.

        Allows the player to choose a gesture and the computer to make a move.
        Determines the winner and updates scores.
        
        Returns:
            str: The result of the round ('win', 'lose', or 'tie').
        """
        # Player and computer choose gestures
        player_gesture = self.player.get_player_gesture()
        self.root.update()
        computer_gesture = self.gesture.make_move()

        if player_gesture != "":
            self.root.update()
            # Create a Round instance to determine the outcome
            round_instance = Round(self.current_round, player_gesture, computer_gesture)
            round_outcome = round_instance.record_outcome(self.gesture)
            # Update the score based on the round outcome
            if round_outcome == "win":
                self.player.update_player_score()
            elif round_outcome == "lose":
                self.computer.update_computer_score()

            # Update GUI with the result of this round
            self.result_label.config(
                text=f"Round {self.current_round}: You chose {player_gesture}, Computer chose {computer_gesture}. Outcome: {round_outcome.capitalize()}."
            )

            self.current_round += 1
            self.player.set_player_gesture("")
            self.update_score()
            return round_outcome
        
    def update_score(self):
        """Displays the current wins for both player and computer on GUI"""
                # Update GUI with the result of this round
        self.score_label.config(
            text=f"Current score - Player: {self.player.get_player_score()}, Computer: {self.computer.get_computer_score()}"
        )
        self.root.update()

    def handle_player_move(self, player_gesture):
        """Handles the player's gesture through buttons"""
        self.player.set_player_gesture(player_gesture)

    def decide_winner(self):
        """
        Determines the overall game winner based on the scores.

        Returns:
            str: 'player' if the player wins, 'computer' if the computer wins, or 'tie' if it's a draw.
        """
        if self.player.get_player_score() > self.computer.get_computer_score():
            self.player.increase_player_wins()
            return "player"
        elif self.computer.get_computer_score() > self.player.get_player_score():
            self.computer.increase_computer_wins()
            return "computer"
        else:
            return "tie"
    
    def end_game(self):
        """Ends the current game session and announces the winner."""
        self.winner = self.decide_winner()
        if self.winner == "player":
            self.winner_label.config(
            text="Congratulations! You won the game!"
            )
        elif self.winner == "computer":
            self.winner_label.config(
            text="The computer won the game! Better luck next time."
            )
        else:
            self.winner_label.config(
            text="The game is a tie!"
            )
        
        self.display_leaderboard()

    def play_again(self, flag):
        if flag == True:
            self.choice.set("yes")
            self.replay_label.config(text="Starting a new game!")
            self.current_round = 1
            self.player.set_player_score(0)
            self.computer.set_computer_score(0)
            self.update_score()
            self.winner_label.config(text="")
            self.start()
        else:
            self.choice.set("no")
            self.replay_label.config(text="Thank you for playing!")
            self.root.destroy()  # Close GUI completely


    def display_leaderboard(self):
        """Displays the final score of both player and computer."""
        self.display_label.config(
            text=f"Final Leaderboard: {self.player.name}: {self.player.get_player_wins()} Computer: {self.computer.get_computer_wins()}"
        )
    
    def set_choice(self, choice):
        '''Sets choice based on argument'''
        self.choice = choice

    def get_choice(self):
        '''Returns choice'''
        return self.choice

    def start(self):
        """Play a full game with the option to replay."""
        self.setup_gui()
        self.replay_label.config(text="Game started. Make your move.")

        while self.root.winfo_exists():
            while self.current_round <= self.rounds:
                self.play_round()
                self.root.update()  # Allow GUI updates during rounds

            if self.current_round > self.rounds:
                self.replay_label.config(text=" ")
                self.end_game()
                self.replay_button.pack(side=tk.LEFT, padx=5)  # Show the button on round 3
                self.no_button.pack(side=tk.LEFT, padx=5)  # Show the button on round 3

            self.root.wait_variable(self.choice)

            if self.choice.get() == "no":
                break

    def setup_gui(self):
        """Sets up initial GUI for game"""
        # Clear the initial widgets from root
        for widget in self.root.winfo_children():
            widget.destroy()

        # Configure root for the new game window
        self.root.title("Rock Paper Scissors - Main Game")
        self.root.geometry("1000x500")  # Optionally resize the window

        # Welcome label
        self.label = tk.Label(self.root, text=f"Welcome, {self.player.name}! Choose your move.", font=("Helvetica", 14))
        self.label.pack(pady=10)

        # Frame for buttons
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=10)

        # Rock button
        self.rock_button = tk.Button(self.buttons_frame, text="Rock", command=lambda: self.handle_player_move("rock"))
        self.root.update()
        self.rock_button.pack(side=tk.LEFT, padx=5)

        # Paper button
        self.paper_button = tk.Button(self.buttons_frame, text="Paper", command=lambda: self.handle_player_move("paper"))
        self.root.update()
        self.paper_button.pack(side=tk.LEFT, padx=5)

        # Scissors button
        self.scissors_button = tk.Button(self.buttons_frame, text="Scissors", command=lambda: self.handle_player_move("scissors"))
        self.root.update()
        self.scissors_button.pack(side=tk.LEFT, padx=5)

        # Result label
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

        # Score label
        self.score_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.score_label.pack(pady=10)

        self.winner_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.winner_label.pack(pady=10)

        self.display_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.display_label.pack(pady=10)

        self.replay_button = tk.Button(self.buttons_frame, text="Replay (Only click after round is over)?", command=lambda: self.play_again(True))
        self.replay_button.pack(side=tk.LEFT, padx=5)

        self.no_button = tk.Button(self.buttons_frame, text="No", command=lambda: self.play_again(False))
        self.no_button.pack(side=tk.LEFT, padx=5)
        self.no_button.pack_forget()

        self.replay_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.replay_label.pack(pady=10)
        self.replay_button.pack_forget()

def main():
    root = tk.Tk()
    root.geometry("800x600")

    # Mock player and computer
    
    computer = Computer()
    gesture = Gesture()
    player = Player("TestPlayer", "")

    # Instantiate the Game class
    game = Game(root, player, computer, gesture)

    # Test the `start` method, which runs the GUI
    game.start()

    # At this point, manually testing GUI inputs verifies:
    # - play_round()
    # - update_score()
    # - handle_player_move()
    # - end_game()
    # - display_leaderboard()
    # - play_again()

    # After GUI is closed, print the results to test other methods
    print("Testing Game Results:")
    print(f"Player's Final Score: {player.get_player_score()}")
    print(f"Computer's Final Score: {computer.get_computer_score()}")
    print(f"Player's Wins: {player.get_player_wins()}")
    print(f"Computer's Wins: {computer.get_computer_wins()}")

if __name__ == "__main__":
    main()
