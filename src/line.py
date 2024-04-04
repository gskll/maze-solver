from tkinter import BOTH, Canvas


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False

        return self.x == other.x and self.y == other.y


class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color
        )
        canvas.pack(fill=BOTH, expand=1)

    def __repr__(self) -> str:
        return f"Line from {self.start} to {self.end}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Line):
            return False
        return self.start == other.start and self.end == other.end
