def generate_cipher_puzzle(difficulty):
    # Return a puzzle dict
    if difficulty == 'easy':
        return {"type": "cipher", "question": "What is A + 1?", "answer": "B"}
    elif difficulty == 'medium':
        return {"type": "cipher", "question": "What is B + 2?", "answer": "D"}
    else:
        return {"type": "cipher", "question": "What is Z - 2?", "answer": "X"}
