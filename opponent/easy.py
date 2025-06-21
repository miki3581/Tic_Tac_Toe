from .base import BaseAI
import random
import time

random.seed(time.time())


class EasyAI(BaseAI):
    def get_move(self, board):
        empty = [
            (r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
        if not empty:
            return None
        return random.choice(empty)
