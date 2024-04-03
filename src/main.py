from maze import Maze
from window import Window


def main():
    margin = 50
    num_rows = 12
    num_cols = 16
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) // num_cols
    cell_size_y = (screen_y - 2 * margin) // num_rows

    win = Window(screen_y, screen_x)
    maze = Maze(
        margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, window=win
    )
    maze.solve()

    win.wait_for_close()


main()
