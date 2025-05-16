from puzzles.cipher import generate_cipher_puzzle
from puzzles.maze import generate_maze_puzzle
from puzzles.symbol import generate_symbol_puzzle
import random

def get_puzzle_by_type(puzzle_type, difficulty):
    if puzzle_type == 'cipher':
        return generate_cipher_puzzle(difficulty)
    elif puzzle_type == 'maze':
        return generate_maze_puzzle(difficulty)
    elif puzzle_type == 'symbol':
        return generate_symbol_puzzle(difficulty)
    else:
        return None

def get_random_puzzle(difficulty, solved_types):
    all_types = ['cipher', 'maze', 'symbol']
    available = [p for p in all_types if p not in solved_types]

    if not available:
        available = all_types  # All solved, start over randomly

    selected = random.choice(available)
    return get_puzzle_by_type(selected, difficulty)
