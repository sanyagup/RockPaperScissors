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

    def __str__(self):
        """String representation of the game."""
        return f"Game: Rounds: {self.rounds}, Current Round: {self.current_round}"

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
        computer_gesture = self.gesture.make_move()

        # Create a Round instance to determine the outcome
        round_instance = Round(self.current_round, player_gesture, computer_gesture)
        round_outcome = round_instance.record_outcome(self.gesture)

        self.result_label.config(
            text=f"Round {self.current_round}: You chose {player_gesture}, Computer chose {computer_gesture}. Outcome: {round_outcome.capitalize()}."
        )


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
        return round_outcome

    def handle_player_move(self, player_gesture):
        """Handles the player's gesture and completes a game round."""
        self.player.set_player_gesture(player_gesture)

    def decide_winner(self):
        """
        Determines the overall game winner based on the scores.

        Returns:
            str: 'player' if the player wins, 'computer' if the computer wins, or 'tie' if it's a draw.
        """
        if self.player.get_player_score() > self.computer.get_computer_score():
            return "player"
        elif self.computer.get_computer_score() > self.player.get_player_score():
            return "computer"
        else:
            return "tie"

    def update_score(self):
        """Displays the current score for both player and computer."""
                # Update GUI with the result of this round
        self.result_label.config(
            text=f"Current Score - Player: {self.player.get_player_score()}, Computer: {self.computer.get_computer_score()}"
        )


    def track_rounds(self):
        """
        Checks if the game has more rounds to play.

        Returns:
            bool: True if there are more rounds, False otherwise.
        """
        return self.current_round <= self.rounds

    def play_again(self):
        """
        Asks the player if they want to play another game.

        Returns:
            bool: True if the player chooses to play again, False otherwise.
        """
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        return choice == "yes"

    def end_game(self):
        """Ends the current game session and announces the winner."""
        winner = self.decide_winner()
        if winner == "player":
            print("Congratulations! You won the game!")
        elif winner == "computer":
            print("The computer won the game! Better luck next time.")
        else:
            print("The game is a tie!")
        
        self.display_leaderboard()

    def display_leaderboard(self):
        """Displays the final score of both player and computer."""
        print("Final Leaderboard:")
        print(f"{self.player.name}: {self.player.get_player_score()}")
        print(f"Computer: {self.computer.score}")
    
    def start(self):
        """Play a full game with the option to replay"""
        self.setup_gui()
        while True:
            # Play each round until the total rounds are reached
            while self.track_rounds():
                print("in track rounds")
                self.play_round()
                self.update_score()

            # End the game and display the final results
            self.end_game()

            # Check if the player wants to play again
            if not self.play_again():
                print("Thank you for playing!")
                break

    def setup_gui(self):
        # Clear the initial widgets from root
        for widget in self.root.winfo_children():
            widget.destroy()

        # Configure root for the new game window
        self.root.title("Rock Paper Scissors - Main Game")
        self.root.geometry("400x300")  # Optionally resize the window

        # Welcome label
        self.label = tk.Label(self.root, text=f"Welcome, {self.player.name}! Choose your move.", font=("Helvetica", 14))
        self.label.pack(pady=10)

        # Frame for buttons
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=10)

        # Rock button
        self.rock_button = tk.Button(self.buttons_frame, text="Rock", command=lambda: self.handle_player_move("rock"))
        self.rock_button.pack(side=tk.LEFT, padx=5)

        # Paper button
        self.paper_button = tk.Button(self.buttons_frame, text="Paper", command=lambda: self.handle_player_move("paper"))
        self.paper_button.pack(side=tk.LEFT, padx=5)

        # Scissors button
        self.scissors_button = tk.Button(self.buttons_frame, text="Scissors", command=lambda: self.handle_player_move("scissors"))
        self.scissors_button.pack(side=tk.LEFT, padx=5)

        # Result label
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self.root, text=f"Score: {self.player.name}: {self.player.get_player_score()} | Computer: {self.computer.get_computer_score()}", font=("Helvetica", 12))
        self.score_label.pack(pady=10)
