from tkinter import Tk, BOTH, Canvas

from .line import Line


class Window:
    def __init__(self, height: int, width: int):
        self.__root: Tk = Tk()
        self.__canvas: Canvas = Canvas(
            self.__root, height=height, width=width, bg="white"
        )
        self.__running: bool = False

        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas.pack(fill=BOTH, expand=1)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed.")

    def close(self):
        self.__running = False

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.__canvas, fill_color)
