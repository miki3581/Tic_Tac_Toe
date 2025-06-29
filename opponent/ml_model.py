import joblib
import os


class MLModel:
    """
    Klasa do obsługi modelu ML dla gry w kółko-krzyżyk.
    Ładuje model z pliku
    Przewiduje najlepsze ruchy na podstawiestanu planszy.
    """
    def __init__(self):
        """Inicjalizuje model ML, ładując go z pliku."""
        model_path = os.path.join(os.path.dirname(__file__),
                                  'tictactoe_model.pkl')
        self.model = joblib.load(model_path)

    def predict(self, flat_board, player_symbol):
        """
        Oblicza ocenę kadego moliwego ruchu na planszy.

        Args:
            flat_board (list): Płaska reprezentacja planszy (9 elementów).
            player_symbol (str): Symbol gracza ('X' lub 'O').

        Returns:
            list: Lista ocen dla każdego pola na planszy.
        """
        predictions = []
        player_value = 1 if player_symbol == "X" else -1

        for i in range(9):
            if flat_board[i] != 0:
                predictions.append(-1.0)  # zajęte pole
                continue

            temp_board = flat_board.copy()
            temp_board[i] = player_value  # symuluj ruch gracza
            proba = self.model.predict_proba([temp_board])[0]

            label_scores = {
                'X': proba[self.model.classes_.tolist().index('X')],
                '-': proba[self.model.classes_.tolist().index('-')],
                'O': proba[self.model.classes_.tolist().index('O')]
            }

            # Faworyzuj własne zwycięstwo, potem remis
            score = label_scores[player_symbol] + 0.5 * label_scores['-']
            predictions.append(score)

        return predictions
