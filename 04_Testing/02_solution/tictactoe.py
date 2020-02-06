import numpy as np

# Tic-Iac-Toe!

# Write a tic tax toe game


class Game:
    EX = 1
    OH = 2
    PLAYERS = (EX, OH)

    def __init__(self, randomize=False):
        if randomize:
            self.board = np.random.randint(0, 3, size=(3, 3), dtype=int)
        else:
            self.board = np.zeros((3, 3), dtype=int)

    def get_position(self, r, c):
        if r < 0 or r > 2:
            raise ValueError("'r' must be between 0 and 2, inclusive")

        if c < 0 or c > 2:
            raise ValueError("'c' must be between 0 and 2, inclusive")

        return self.board[r, c]

    def place(self, r, c, player):
        if r < 0 or r > 2:
            raise ValueError("'r' must be between 0 and 2, inclusive")

        if c < 0 or c > 2:
            raise ValueError("'c' must be between 0 and 2, inclusive")

        if self.board[r, c] != 0:
            raise ValueError("Can't play there!")

        if player not in self.PLAYERS:
            raise ValueError("Unknown player ID %i" % player)

        self.board[r, c] = player

    def is_valid_board(self):
        """Return True if this is a valid game board."""
        num_ex = np.sum(self.board == self.EX)
        num_oh = np.sum(self.board == self.OH)
        winner = self.get_winning_player()

        # check for a valid number of player moves
        if np.abs(num_ex - num_oh) > 1:
            return False

        # check that there aren't two winners or that the winner hasn't won in two different ways
        if winner is not None:
            # clone the game and check, by removing the winning player, that the other player hasn't also won
            clone = Game()
            clone.board[...] = self.board  # copy board
            clone.board[clone.board == winner] = 0  # remove first winner

            if clone.get_winning_player() is not None:
                return False

            # check that the winner hasn't won twice
            if np.sum(self.board == winner) == 5:
                # check if the winner has one in a row and a column at once
                for r, c in np.ndindex(3, 3):
                    if np.all(self.board[r, :] == winner) and np.all(self.board[:, c] == winner):
                        return False

                # check where the winner has won in an X-shape
                if np.all(self.board[[0, 0, 1, 2, 2], [0, 2, 1, 0, 2]] == winner):
                    return False

        return True

    def get_winning_player(self):
        # check rows and columns
        for r in range(3):
            row = self.board[r, :]
            col = self.board[:, r]

            for p in self.PLAYERS:
                if all(x == p for x in row):
                    return p

            for p in self.PLAYERS:
                if all(x == p for x in col):
                    return p

        # check diagonals
        for p in self.PLAYERS:
            if all(x == p for x in (self.board[0, 0], self.board[1, 1], self.board[2, 2])):
                return p

            if all(x == p for x in (self.board[0, 2], self.board[1, 1], self.board[2, 0])):
                return p

    def __str__(self):
        symbols = [".", "X", "O"]

        rows = ["+-------+"]
        for c in range(3):
            row = ["|"]
            for r in range(3):
                row.append(symbols[self.board[r, c]])

            row.append("|")
            rows.append(" ".join(row))

        rows.append("+-------+")

        return "\n".join(rows)


def play_random_game():
    """
    Plays tic tac toe by placing alternating markers randomly on the board until it's full or one of the players wins.
    """
    game = Game()
    positions = list(np.ndindex(3, 3))  # all valid positions on the board
    move = 0

    np.random.shuffle(positions)  # randomly re-arrange the order of positions played

    while move < len(positions) and game.get_winning_player() is None:
        r, c = positions[move]
        game.place(r, c, game.PLAYERS[move % 2])
        move += 1

    return game


if __name__ == "__main__":
    print(play_random_game())
