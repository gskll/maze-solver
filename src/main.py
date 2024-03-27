from src.models import Window, Cell


def main():
    win = Window(800, 600)

    cell_top = Cell(
        win,
        10,
        10,
        10,
        has_right_wall=False,
        has_bottom_wall=False,
        has_left_wall=False,
    )
    cell_top.draw()

    cell_bottom = Cell(
        win, 25, 10, 10, has_left_wall=False, has_right_wall=False, has_top_wall=False
    )
    cell_bottom.draw()

    cell_right = Cell(
        win, 40, 10, 10, has_top_wall=False, has_left_wall=False, has_bottom_wall=False
    )
    cell_right.draw()

    cell_left = Cell(
        win, 55, 10, 10, has_top_wall=False, has_right_wall=False, has_bottom_wall=False
    )
    cell_left.draw()

    cell_top_and_left = Cell(
        win, 10, 50, 10, has_right_wall=False, has_bottom_wall=False
    )
    cell_top_and_left.draw()

    cell_top_and_bottom = Cell(
        win, 25, 50, 10, has_right_wall=False, has_left_wall=False
    )
    cell_top_and_bottom.draw()

    cell_top_and_right = Cell(
        win, 40, 50, 10, has_bottom_wall=False, has_left_wall=False
    )
    cell_top_and_right.draw()

    cell_bottom_and_left = Cell(
        win, 55, 50, 10, has_top_wall=False, has_right_wall=False
    )
    cell_bottom_and_left.draw()

    cell_bottom_and_right = Cell(
        win, 70, 50, 10, has_left_wall=False, has_top_wall=False
    )
    cell_bottom_and_right.draw()

    cell_left_and_right = Cell(
        win, 85, 50, 10, has_top_wall=False, has_bottom_wall=False
    )
    cell_left_and_right.draw()

    cell_no_top = Cell(win, 10, 90, 10, has_top_wall=False)
    cell_no_top.draw()

    cell_no_bottom = Cell(win, 25, 90, 10, has_bottom_wall=False)
    cell_no_bottom.draw()

    cell_no_right = Cell(win, 40, 90, 10, has_right_wall=False)
    cell_no_right.draw()

    cell_no_left = Cell(win, 55, 90, 10, has_left_wall=False)
    cell_no_left.draw()

    cell_all = Cell(win, 10, 130, 10)
    cell_all.draw()
    cell_all_2 = Cell(win, 25, 130, 10)
    cell_all_2.draw()
    cell_all_3 = Cell(win, 35, 130, 10)
    cell_all_3.draw()
    cell_all_4 = Cell(win, 25, 140, 10)
    cell_all_4.draw()

    cell_all.draw_move(cell_all_2)
    cell_all_3.draw_move(cell_all_4)
    cell_no_left.draw_move(cell_no_right, undo=True)

    win.wait_for_close()


main()
