# %%
import sys
import numpy as np

# %%

DIFFICULTY_MAP = {
    0: {
        "Level": "Beginner",
        "Shape": (9, 9),
        "Mines": 10
    },
    1: {
        "Level": "Intermediate",
        "Shape": (16, 16),
        "Mines": 40
    },
    2: {
        "Level": "Advanced",
        "Shape": (24, 24),
        "Mines": 99
    }
}

# %%


class MineSweeper():
    def __init__(self, difficulty, seed=None) -> None:

        self.rng = np.random.default_rng(seed=seed)

        diff_map = DIFFICULTY_MAP[difficulty]
        self.difficulty = difficulty
        self.level = diff_map["Level"]
        self.shape = diff_map["Shape"]
        self.mines = diff_map["Mines"]

        self.board = np.full(self.shape, "-")
        self.true_board = self._make_board()

    def _make_board(self):
        mines = self.rng.choice(self.board.size, self.mines)
        true_board = np.full(self.board.size, False)
        true_board[mines] = True
        true_board = true_board.reshape(self.shape)
        return true_board

    def display(self, cheat=False):
        if cheat:
            cheat_board = self.board.copy()
            cheat_board[self.true_board] = "*"
            np.savetxt(sys.stdout, cheat_board, fmt="%s")
        else:
            np.savetxt(sys.stdout, self.board, fmt="%s")
