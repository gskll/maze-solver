from tkinter import Tk, BOTH, Canvas

from line import Line


class Window:
    def __init__(self, height: int, width: int):
        self._bg_color = "gray3"
        self._root: Tk = Tk()
        self._canvas: Canvas = Canvas(
            self._root, height=height, width=width, bg=self._bg_color
        )
        self._running: bool = False

        self._root.title("Maze Solver")
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._canvas.pack(fill=BOTH, expand=1)

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()
        print("Window closed.")

    def close(self):
        self._running = False

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self._canvas, fill_color)
