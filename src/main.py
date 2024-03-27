from src.models import Window, Maze


def main():
    win = Window(800, 600)

    Maze(win, 10, 10, 10, 10, 30)

    win.wait_for_close()


main()
