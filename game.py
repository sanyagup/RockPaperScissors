from round import Round
from player import Player
from computer import Computer
from gesture import Gesture

class Game:
    """
    Sanya Gupta
    Represents the Rock, Paper, Scissors game."""

    def __init__(self, player, computer, gesture, rounds=3):
        """Initialize the game with a player, a computer, and number of rounds."""
        self.rounds = rounds
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
        player_gesture = self.gesture.choose_gesture()
        computer_gesture = self.gesture.make_move()

        # Create a Round instance to determine the outcome
        round_instance = Round(self.current_round, player_gesture, computer_gesture)
        round_outcome = round_instance.record_outcome(self.gesture)

        # Update the score based on the round outcome
        if round_outcome == "win":
            self.player.update_player_score()
        elif round_outcome == "lose":
            self.computer.update_computer_score()

        # Print the outcome and increment the round counter
        print(f"Round {self.current_round}: Player chose {player_gesture}, Computer chose {computer_gesture}")
        print(f"Round Outcome: {round_outcome}")

        self.current_round += 1
        return round_outcome


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
        print(f"Current Score - Player: {self.player.get_player_score()}, Computer: {self.computer.get_computer_score()}")

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

def main():
    """
    Tests the Game class by initializing a player and computer, then playing a full game.

    This function:
        1. Initializes Player and Computer objects.
        2. Creates a Game object and plays rounds until all rounds are complete.
        3. Ends the game and displays the final leaderboard.
        4. Asks if the player wants to play another game.

    Returns:
        None
    """


    # Initialize player and computer
    name = input("Enter your name: ")
    player = Player(name)
    computer = Computer()
    gesture = Gesture()

    # Play a full game with the option to replay
    while True:
        game = Game(player, computer, gesture, rounds=3)
        print(game)

        # Play each round until the total rounds are reached
        while game.track_rounds():
            game.play_round()
            game.update_score()

        # End the game and display the final results
        game.end_game()

        # Check if the player wants to play again
        if not game.play_again():
            print("Thank you for playing!")
            break


if __name__ == "__main__":
    main()



