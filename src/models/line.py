from tkinter import BOTH, Canvas


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(
            self.start.x, self.end.x, self.start.y, self.end.y, fill=fill_color
        )
        canvas.pack(fill=BOTH, expand=1)
