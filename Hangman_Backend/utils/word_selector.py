import random

def load_words_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Paths to word files
EASY_MEDIUM_WORDS_PATH = r'D:\HANGMAN_GAME\Hangman_Backend\database\words_alpha.txt'
HARD_WORDS_PATH = r'D:\HANGMAN_GAME\Hangman_Backend\database\words.txt'


# Load words from the files
easy_medium_words = load_words_from_file(EASY_MEDIUM_WORDS_PATH)
hard_words = load_words_from_file(HARD_WORDS_PATH)

def select_random_word(difficulty):
    """Select a word based on the difficulty level."""
    if difficulty == 'hard':
        return random.choice(hard_words)
        print(hard_words)
    else:  # default to easy/medium
        return random.choice(easy_medium_words)
        print(easy_medium_words)