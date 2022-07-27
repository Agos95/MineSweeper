# %%
from time import sleep
import argparse
import curses

# %%


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int,
                        help="pad width", default=10)
    parser.add_argument("--height", type=int,
                        help="pad height", default=10)

    return vars(parser.parse_args())


# %%


def main(args):
    w, h = args["width"], args["height"]
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    pad = curses.newpad(h, w)
    for y in range(h - 1):
        for x in range(w - 1):
            pad.addch(y, x, "-")
    pad.addch("-")
    pad.refresh(0, 0, 0, 0, curses.LINES, curses.COLS)

    sleep(5)

    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()


# %%

if __name__ == "__main__":
    args = parse_args()
    main(args)
