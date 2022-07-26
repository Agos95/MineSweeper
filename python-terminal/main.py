# %%

import argparse
from minesweeper import MineSweeper

# %%


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--difficulty", choices=[0, 1, 2], default=0, type=int,
                        help="Select difficulty:\n" +
                        "\t0 -> Beginner     ( 9x9 , 10 Mines)" +
                        "\t1 -> Intermediate (16x16, 40 Mines)" +
                        "\t0 -> Advanced     (24x24, 99 Mines)")
    return vars(parser.parse_args())

# %%


def main():
    args = parse_args()
    game = MineSweeper(args["difficulty"])
    game.display(cheat=True)


# %%


if __name__ == "__main__":
    main()
