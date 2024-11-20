from gesture import Gesture

class Round:
    """
    Sanya Gupta
    CMSY 257
    Represents a single round in the game."""

    def __init__(self, round_number, player_gesture=None, computer_gesture=None):
        """Initialize a round with round number, player gesture, and computer gesture."""
        self.round_number = round_number
        self.player_gesture = player_gesture
        self.computer_gesture = computer_gesture
        self.outcome = None

    def __str__(self):
        """Provides a string representation of the round, including the round number and outcome."""
        return f"Round: {self.round_number}, Outcome: {self.outcome}"


    def record_outcome(self, gesture):
        """
        Records the outcome of the round based on the result of `compare_gestures`.
        
        Sets:
            self.outcome (str): The outcome of the round ('win', 'lose', or 'tie').
        
        Returns:
            str: The outcome of the round.
        """
        self.outcome = gesture.compare_gestures(self.player_gesture, self.computer_gesture)
        return self.outcome

    def determine_winner(self):
        """
        Determines the winner of the round based on the recorded outcome.
        
        Returns:
            str: 'player' if the player wins, 'computer' if the computer wins, 'none' if it's a tie.
        """
        if self.outcome == "win":
            return "player"
        elif self.outcome == "lose":
            return "computer"
        else:
            return "none"