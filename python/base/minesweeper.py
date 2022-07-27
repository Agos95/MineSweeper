# %%
import random

# %%


class MineSweeper():

    DIFFICULTY_LEVEL = {
        0: {
            "level": "Beginner",
            "shape": (9, 9),
            "mines": 10
        },
        1: {
            "level": "Intermediate",
            "shape": (16, 16),
            "mines": 40
        },
        2: {
            "level": "Advanced",
            "shape": (24, 24),
            "mines": 99
        }
    }

    def __init__(self, difficulty=0, fair=True, seed=None) -> None:
        """
        Parameters
        ----------

        difficulty : int, default 0
            Difficulty level; must be in [0,1,2], otherwise it deafults to 0.
        fair : bool, default True
            If True, board is created after first move, to assure that it is always safe.
            Otherwise, board is created immediately.
        seed : int, optional
            Seed to initialize the rng for reproducible boards.
        """

        # initialize rng
        self.rng = random.Random(seed)

        # game options
        self.level = self.DIFFICULTY_LEVEL[difficulty]["level"]
        self.rows, self.cols = self.DIFFICULTY_LEVEL[difficulty]["shape"]
        self.mines = self.DIFFICULTY_LEVEL[difficulty]["mines"]

        # display options
        self.header = [f"{i:2d}" for i in range(self.cols)]
        self.index = [f"{i:2d}" for i in range(self.rows)]

        self.board = [[" -"] * self.cols for _ in range(self.rows)]

        if not fair:
            self._make_board()
        else:
            self.true_board = None

        # win/loss
        self.available_moves = self.rows * self.cols - self.mines
        self.win = False
        self.loss = False

    def play(self) -> None:
        self.display()
        while True:
            row, col = self._get_move()
            if self.true_board is None:
                self._make_board(safe=(row, col))
            self._update(row, col)
            self.display()
            if self.loss or self.win:
                break

        if self.loss:
            print("You Loose!")
            x = input("Do you want to see the solution? [y/n] ")
            if x.strip().lower() == "y":
                self.cheat()

        if self.win:
            print("You win!")

        return

    def _make_board(self, safe=None) -> None:
        """
        Creates the

        Parameters
        ----------
        safe : tuple (row, col), optional
            If not None, it represents a safe position where a mine cannot be placed.
        """

        self.true_board = [[" -"] * self.cols for _ in range(self.rows)]
        # get list of all positions (row, col) in the board
        pos = [(row, col) for row in range(self.cols)
               for col in range(self.cols)]
        # remove safe spot if present
        if safe is not None:
            pos.remove(safe)
        # get random bomb positions
        pos = self.rng.sample(pos, k=self.mines)
        # place bombs in true board
        for (row, col) in pos:
            self.true_board[row][col] = " *"
        # fill true board with the solution
        # each cell is a number indicating how many bombs there are in adjacent cells
        for row in range(self.rows):
            for col in range(self.cols):
                self.true_board[row][col] = self._count_mines(row, col)

    def _is_valid(self, row, col):
        return True if row in range(self.rows) and col in range(self.cols) else False

    def _count_mines(self, row, col) -> str:
        """
        Counts number of mines in adjacent cells.

        Parameters
        ----------
        row : int
            Row index
        col : int
            Column index

        Returns
        -------
        str
            String representing the number of bombs in adjacent cells.
        """
        if self.true_board[row][col] == " *":
            return " *"
        else:
            cnt = 0
            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    if self._is_valid(r, c) and self.true_board[r][c] == " *":
                        cnt += 1
            return f"{cnt:2d}"

    def _get_move(self):
        """
        Request and process a move by the user.
        """

        row, col = None, None
        valid, _ = self._check_input(row, col)
        while not valid:
            move = input("Move (row col): ")
            row, col = [int(x) for x in move.strip().split(" ")]
            valid, error = self._check_input(row, col)
            if error is not None:
                print(error)
        return row, col

    def _check_input(self, row, col):

        if not self._is_valid(row, col):
            error = f"({row}, {col}) is not valid: grid size is {self.rows}x{self.cols}."
            return False, error

        elif not self.board[row][col] == " -":
            error = f"({row}, {col}) is already discovered: select an unknown cell."
            return False, error

        else:
            return True, None

    def _update(self, row, col) -> None:
        coords = [(row, col)]
        n_moves = 0  # count number of discovered cells with this move
        bombs = ""
        while coords:
            row, col = coords.pop()
            bombs = self.true_board[row][col]
            if self.board[row][col] == " -":
                self.board[row][col] = bombs
                n_moves += 1
                # if there are no adjacent bombs, search recursively in the neighbours
                if bombs == " 0":
                    coords += [(r, c) for r in range(row - 1, row + 2)
                               for c in range(col - 1, col + 2) if self._is_valid(r, c) and (r, c) != (row, col)]

        # update the number of available moves
        self.available_moves -= n_moves

        # check win/loss
        if self.available_moves == 0:
            self.win = True
        if bombs == " *":
            self.loss = True

    def display(self) -> str:
        """
        Display the current board.
        """
        board_str = f"    {' '.join(self.header)}\n"
        board_str += f"   ┌{'─'*(len(board_str)-5)}\n"

        for i in range(self.rows):
            board_str += f"{self.index[i]} │{' '.join(self.board[i])}\n"
        board_str += "\n"
        print(board_str)

    def cheat(self) -> str:
        """
        Display the solution board.
        """
        board_str = f"    {' '.join(self.header)}\n"
        board_str += f"   ┌{'─'*(len(board_str)-5)}\n"

        for i in range(self.rows):
            board_str += f"{self.index[i]} │{' '.join(self.true_board[i])}\n"
        print(board_str)

# %%
