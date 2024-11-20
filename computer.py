from gesture import Gesture

class Computer:
    """
    Sanya Gupta
    CMSY 257
    Represents a computer opponent in the Rock, Paper, Scissors game.
    
    An instance of this class represents the computer's role in the game, including its difficulty
    level, score, and the gesture it chooses in each round.
    """

    def __init__(self):
        """
        Initializes the computer with a score and a current gesture.
        """
        self.score = 0
        self.current_gesture = None
        self.wins = 0

    def __str__(self):
        """Provides a string representation of the computer showing its difficulty level and score."""
        return f"Computer Score: {self.score}"

    def get_computer_score(self):
        """Gets the current score of the player."""
        return self.score
    
    def update_computer_score(self):
        """
        Increments the computer's score by one point.
    
        Returns:
            int: The updated score of the computer.
        """
        self.score += 1
        return self.score
    
    def increase_computer_wins(self):
        self.wins += 1
    
    def get_computer_wins(self):
        return self.wins

    def set_computer_score(self, score):
        self.score = score


    
def main():
    """
    Tests the Computer class methods, including make_move, choose_random_gesture, and choose_gesture_based_on_strategy.
    
    This function:
        1. Initializes a Computer object and Gesture Object.
        2. Tests the make_move method by calling it multiple times and printing the chosen gestures.
        3. Tests the choose_random_gesture method by calling it multiple times and printing the chosen
        gestures.
        4. Tests the choose_gesture_based_on_strategy method by calling it multiple times and printing
        the chosen gestures.

    Returns:
        None
    """
    # Initialize a computer with hard difficulty
    computer = Computer()
    gesture = Gesture()
    print(computer)  # Display initial computer details

    # Test make_move based on difficulty
    move = gesture.make_move()
    print(f"Computer's chosen move (using make_move): {move}")
    print(computer)  # Show updated computer state after move

    # Test choose_random_gesture directly
    random_move = gesture.return_random_gesture()
    print(f"Computer's random move: {random_move}")
    print(computer)  # Show updated state

    #Check if score is incrementing
    updated_score = computer.update_computer_score()
    print(f"Updated computer score: {updated_score}")

    #Display final results
    print(computer)

if __name__ == "__main__":
    main()