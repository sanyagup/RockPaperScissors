from gesture import Gesture

class Player:
    """
    Sanya Gupta
    Represents a player in the game."""

    def __init__(self, name, player_gesture):
        """Initialize a player with a name, score, and current gesture."""
        self.name = name
        self.score = 0
        self.player_gesture = player_gesture
        self.wins = 0


    def __str__(self):
        """Provides a string representation of the player showing their name and score."""
        return f"Player: {self.name}, Score: {self.score}"
    
    def increase_player_wins(self):
        self.wins += 1
    
    def get_player_wins(self):
        return self.wins

    def update_player_score(self):
        """
        Increments the player's score by one point.
    
        Returns:
            int: The updated score of the player.
        """
        self.score += 1
        return self.score
    
    def get_player_score(self):
        """Gets the current score of the player."""
        return self.score
    
    def set_player_gesture(self, player_gesture):
        self.player_gesture = player_gesture
    
    def get_player_gesture(self):
        return self.player_gesture
    
    def set_player_score(self, score):
        self.score = score

# def main():
#     """
#     Tests the Player class methods including choose_gesture, validate_move, make_move, and update_score.
    
#     This function:
#         1. Initializes a Player object with the name "Alice" and intializes gesture object.
#         2. Calls the choose_gesture method from the Gestures Class to select a random gesture.
#         3. Validates the chosen gesture.
#         4. Makes a move by calling the make_move method.
#         5. Updates the player's score.
#         6. Prints the player's name and score.
    
#     Returns:
#         None
#     """
#     # Initialize a player
#     player = Player("Alice")
#     print(player)  # Display initial player details
#     gesture = Gesture()

#     # Test choose_gesture method
#     chosen_gesture = gesture.choose_gesture()
#     print(f"Player chose: {chosen_gesture}")

#     # Test validate_move method
#     is_valid = gesture.validate_move(chosen_gesture)
#     print(f"Is the chosen gesture valid? {is_valid}")

#     # Test update_score method
#     updated_score = player.update_score()
#     print(f"Player's updated score: {updated_score}")

#     # Display final player details
#     print(player)

# if __name__ == "__main__":
#     main()

