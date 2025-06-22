import joblib
import os


class MLModel:
    def __init__(self):
        model_path = os.path.join(os.path.dirname(__file__),
                                  'tictactoe_model.pkl')
        self.model = joblib.load(model_path)

    def predict(self, flat_board):
        predictions = []
        for i in range(9):
            if flat_board[i] != 0:
                predictions.append(-1.0)  # zajęte pole
                continue

            temp_board = flat_board.copy()
            temp_board[i] = 1  # zakładamy, że AI gra jako 'X' (1)
            proba = self.model.predict_proba([temp_board])[0]

            label_scores = {
                'X': proba[self.model.classes_.tolist().index('X')],
                '-': proba[self.model.classes_.tolist().index('-')],
                'O': proba[self.model.classes_.tolist().index('O')]
            }

            score = label_scores['X'] + 0.5 * label_scores['-']
            predictions.append(score)

        return predictions
