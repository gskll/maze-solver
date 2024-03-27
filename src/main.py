from src.models import Window, Maze


def main():
    win = Window(800, 600)

    num_rows = 3
    num_cols = 6
    Maze(10, 10, num_rows, num_cols, 30, window=win)

    win.wait_for_close()


main()
