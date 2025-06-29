import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os


def parse_move(move):
    """Konwertuje ruch w formacie 'row-col' na indeks planszy 0-8."""
    if move == '---':
        return None
    row, col = map(int, move.split('-'))
    return row * 3 + col


def moves_to_board(moves, symbol_first='X'):
    """
    Konwertuje listę ruchów na wektor reprezentujący stan planszy.

    Args:
        moves (list): Lista ruchów w formacie 'row-col'.
        symbol_first (str): Symbol gracza rozpoczynającego ('X' lub 'O').

    Returns:
        list: Lista stanu planszy, gdzie 1 oznacza 'X', -1 oznacza 'O',
              a 0 oznacza puste pole.
    """
    board = [0] * 9
    symbols = ['X', 'O'] * 5
    for i, move in enumerate(moves):
        idx = parse_move(move)
        if idx is not None:
            board[idx] = 1 if symbols[i] == symbol_first else -1
    return board


def train_and_save_model(csv_path=None, model_path='tictactoe_model.pkl'):
    """
    Trenuje model ML na podstawie danych z pliku CSV
    i zapisuje go do pliku.

    Args:
        csv_path (str): Ścieżka do pliku CSV z danymi gier.
        model_path (str): Ścieżka do pliku, w którym zostanie zapisany model.
    """
    csv_path = os.path.join(os.path.dirname(__file__), "tictactoe_games.csv")
    model_path = os.path.join(os.path.dirname(__file__), 'tictactoe_model.pkl')
    df = pd.read_csv(csv_path)

    X = []
    y = []

    for _, row in df.iterrows():
        board = moves_to_board(row[1:])
        if len(board) == 9:
            X.append(board)
            y.append(row['Winner'])

    X = np.array(X)
    y = np.array(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                        random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)
    print(f"Model accuracy: {accuracy * 100:.2f}%")

    joblib.dump(model, model_path)


if __name__ == '__main__':
    train_and_save_model()
