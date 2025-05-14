from utils.word_selector import select_random_word


class GameEngine:
    def __init__(self, difficulty='medium'):
        self.difficulty = difficulty
        self.reset_game()

    def reset_game(self):
        """Reset the game with a new word based on difficulty."""
        self.word = select_random_word(self.difficulty)
        self.guesses = set()
        self.correct_guesses = set()
        self.remaining_attempts = 1  # One attempt for each puzzle
        self.game_over = False
        self.hidden_word = '_' * len(self.word)  # Hidden word to show to the user

    def guess(self, letter):
        """Process a letter guess."""
        if self.game_over:
            return "Game over. Resetting game."

        if letter in self.guesses:
            return "Already guessed this letter."

        self.guesses.add(letter)

        if letter in self.word:
            self.correct_guesses.add(letter)
            self.update_hidden_word()
            if set(self.word) == self.correct_guesses:
                self.game_over = True
                return "You win! Word is: " + self.word
            return f"Correct! Current word: {self.hidden_word}"
        else:
            self.remaining_attempts -= 1
            if self.remaining_attempts <= 0:
                self.game_over = True
                return f"You lose. The word was: {self.word}"
            return f"Incorrect! {self.remaining_attempts} attempts left."

    def update_hidden_word(self):
        """Update the hidden word with the correctly guessed letters."""
        self.hidden_word = ''.join([letter if letter in self.correct_guesses else '_' for letter in self.word])
