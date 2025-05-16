# models/difficulty_predictor.py

class DifficultyPredictor:
    def __init__(self):
        # Load model here in future if needed
        pass

    def predict_difficulty(self, age, performance):
        """
        Takes in user age and performance stats to predict difficulty level.
        """
        if performance['successes'] > 5 and age >= 18:
            return 'hard'
        elif age < 18 or performance['failures'] > 3:
            return 'easy'
        return 'medium'
