from src.models import Window, Line, Point


def main():
    win = Window(800, 600)
    l1 = Line(Point(10, 100), Point(20, 200))
    l2 = Line(Point(50, 500), Point(300, 60))
    win.draw_line(l1, "red")
    win.draw_line(l2, "green")
    win.wait_for_close()


main()
