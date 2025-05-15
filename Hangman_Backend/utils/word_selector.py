import random

EASY_MEDIUM_WORDS_PATH = r'D:\HANGMAN_GAME\Hangman_Backend\database\words_alpha.txt'
HARD_WORDS_PATH = r'D:\HANGMAN_GAME\Hangman_Backend\database\words.txt'

def load_words(path):
    with open(path, 'r') as file:
        words = [line.strip() for line in file if line.strip().isalpha()]
    return words

def select_random_word(difficulty='medium'):
    if difficulty.lower() in ['easy', 'medium']:
        word_list = load_words(EASY_MEDIUM_WORDS_PATH)
    else:
        word_list = load_words(HARD_WORDS_PATH)

    if not word_list:
        raise ValueError("Word list is empty or file not found.")

    selected_word = random.choice(word_list).lower()
    return selected_word

def load_words(path):
    try:
        with open(path, 'r') as file:
            return [line.strip() for line in file if line.strip().isalpha()]
    except FileNotFoundError:
        print(f"Warning: File at {path} not found.")
        return []

DEFAULT_WORDS = ['default', 'hangman', 'puzzle']

def select_random_word(difficulty='medium'):
    if difficulty.lower() in ['easy', 'medium']:
        word_list = load_words(EASY_MEDIUM_WORDS_PATH)
    else:
        word_list = load_words(HARD_WORDS_PATH)

    if not word_list:
        word_list = DEFAULT_WORDS
        print("Warning: Falling back to default word list.")

    return random.choice(word_list).lower()


