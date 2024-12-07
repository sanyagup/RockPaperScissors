import random

class Gesture:
    """
    Sanya Gupta
    CMSY 257

    Represents Gestures within Rock, Paper, Scissors game. 
    
    This class defines shared constants for the Rock, Paper, Scissors game. 

    These methods defined here are used throughout the various classes in the game 
    to ensure consistency and avoid redundancy. Any updates to the game's gestures 
    can be made here, and they will automatically apply to all parts of the program 
    that reference this class.

    Constants:
        GESTURES (list): A list of valid gestures for the game.
    """

    def __init__(self):
        """
        Initializes a list with available gestures.
        """
        self.GESTURES = ["rock", "paper", "scissors"]

    def validate_move(self, gesture):
        """
        Validates if the player's chosen gesture is one of the allowed options.
        
        Parameters:
            gesture (str): The gesture chosen by the player to validate.
        
        Returns:
            bool: True if the gesture is valid; False otherwise.
        """
        return gesture in ['rock', 'paper', 'scissors']
            
    def return_random_gesture(self):
        """Return a random gesture from the list of valid gestures."""
        return random.choice(self.GESTURES)
    
    def choose_gesture(self):
        """Return a user chosen gesture from the list of valid gestures."""
        while True:
            gesture = input(f"Choose a gesture ({', '.join(self.GESTURES)}): ").lower()
            if gesture in self.get_GESTURES():
                self.current_gesture = gesture
                return gesture
            print("Invalid choice. Please choose again.")

    def get_GESTURES(self):
        """Return a the list of valid gestures."""
        return self.GESTURES
    
    def make_move(self):
        """
        Makes a move by choosing a gesture.
        
        Returns:
            str: The gesture chosen by the computer (e.g., 'rock', 'paper', 'scissors').
        """
        return self.return_random_gesture()

    def compare_gestures(self, player_gesture, computer_gesture):
        """
        Compares the gestures of the player and computer to determine the result.
        
        Returns:
            str: 'win' if the player wins, 'lose' if the computer wins, and 'tie' if it's a draw.
        """
        if player_gesture == computer_gesture:
            return "tie"
        elif (player_gesture == "rock" and computer_gesture == "scissors") or \
                (player_gesture == "scissors" and computer_gesture == "paper") or \
                (player_gesture == "paper" and computer_gesture == "rock"):
            return "win"
        else:
            return "lose"
        
def main():
    """
    Tests the Gesture class methods, including validate_move, return_random_gesture, 
    choose_gesture, make_move, and compare_gestures.
    """
    # Step 1: Initialize the Gesture object
    gesture_obj = Gesture()
    
    # Step 2: Test get_GESTURES method
    print("Available gestures:", gesture_obj.get_GESTURES())
    
    # Step 3: Test validate_move method
    test_gesture = "rock"
    print(f"Is '{test_gesture}' a valid move? {gesture_obj.validate_move(test_gesture)}")
    
    invalid_gesture = "fire"
    print(f"Is '{invalid_gesture}' a valid move? {gesture_obj.validate_move(invalid_gesture)}")
    
    # Step 4: Test return_random_gesture method
    random_gesture = gesture_obj.return_random_gesture()
    print(f"Randomly selected gesture: {random_gesture}")
    
    # Step 5: Test choose_gesture method (uncomment this to allow user input)
    # print("Let's choose a gesture:")
    # chosen_gesture = gesture_obj.choose_gesture()
    # print(f"You chose: {chosen_gesture}")
    
    # Step 6: Test make_move method
    computer_gesture = gesture_obj.make_move()
    print(f"Computer's move: {computer_gesture}")
    
    # Step 7: Test compare_gestures method
    player_gesture = "rock"
    print(f"Comparing gestures: Player - {player_gesture}, Computer - {computer_gesture}")
    result = gesture_obj.compare_gestures(player_gesture, computer_gesture)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()