# puzzles/maze.py

def generate_maze_puzzle(difficulty):
    if difficulty == 'easy':
        return {"type": "maze", "question": "Reach the end of a 3x3 maze", "answer": "RRDD"}
    elif difficulty == 'medium':
        return {"type": "maze", "question": "Navigate 4x4", "answer": "RRDDLL"}
    else:
        return {"type": "maze", "question": "5x5 grid puzzle", "answer": "RRDRDL"}
