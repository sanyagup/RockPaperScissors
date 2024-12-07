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
        
def main():
    """
    Tests the Round class methods, including record_outcome and determine_winner.

    This function:
        1. Creates a Round object.
        2. Sets player and computer gestures.
        3. Records the outcome using Gesture's compare_gestures method.
        4. Determines the winner of the round.
        5. Prints the round number, gestures, outcome, and winner.
    """
    # Step 1: Initialize the gestures
    player_gesture = "Rock"
    computer_gesture = "Scissors"

    # Step 2: Create a Round object
    round_number = 1
    round_obj = Round(round_number=round_number, 
                      player_gesture=player_gesture, 
                      computer_gesture=computer_gesture)

    # Step 3: Initialize the Gesture object
    gesture = Gesture()

    # Step 4: Record the outcome
    print(f"--- Round {round_number} ---")
    print(f"Player gesture: {player_gesture}")
    print(f"Computer gesture: {computer_gesture}")
    outcome = round_obj.record_outcome(gesture)
    print(f"Outcome of the round: {outcome}")

    # Step 5: Determine the winner
    winner = round_obj.determine_winner()
    print(f"Winner of the round: {winner}")

    # Step 6: Display round details using __str__
    print(round_obj)

if __name__ == "__main__":
    main()