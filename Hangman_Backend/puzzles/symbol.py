# puzzles/symbol.py

def generate_symbol_puzzle(difficulty):
    if difficulty == 'easy':
        return {"type": "symbol", "question": "Find the symbol for water (H2O)", "answer": "H2O"}
    elif difficulty == 'medium':
        return {"type": "symbol", "question": "What does % represent?", "answer": "percent"}
    else:
        return {"type": "symbol", "question": "What is the symbol for pi?", "answer": "π"}
