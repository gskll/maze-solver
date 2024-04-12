from typing import Callable
from line import Line, Point


class Cell:
    def __init__(
        self,
        x: int,
        y: int,
        size_x: int,
        size_y: int,
        colors: dict[str, str],
        draw_callback: Callable[[Line, str], None] | None = None,
    ) -> None:
        top_left = Point(x, y)
        top_right = Point(x + size_x, y)
        bottom_left = Point(x, y + size_y)
        bottom_right = Point(x + size_x, y + size_y)
        center = Point(x + size_x // 2, y + size_y // 2)

        self._colors = colors
        self._draw_callback = draw_callback
        self._center_point = center
        self._top_wall = Line(top_left, top_right)
        self._right_wall = Line(top_right, bottom_right)
        self._bottom_wall = Line(bottom_left, bottom_right)
        self._left_wall = Line(top_left, bottom_left)

        self._top_wall_midpoint = Point(x + (size_x // 2), y)
        self._bottom_wall_midpoint = Point(x + (size_x // 2), y + size_y)

        self.visited = False
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True

    def draw(self) -> None:
        if self._draw_callback is None:
            return

        if self.has_top_wall:
            self._draw_callback(self._top_wall, self._colors["wall"])
        else:
            self._draw_callback(self._top_wall, self._colors["bg"])

        if self.has_right_wall:
            self._draw_callback(self._right_wall, self._colors["wall"])
        else:
            self._draw_callback(self._right_wall, self._colors["bg"])

        if self.has_bottom_wall:
            self._draw_callback(self._bottom_wall, self._colors["wall"])
        else:
            self._draw_callback(self._bottom_wall, self._colors["bg"])

        if self.has_left_wall:
            self._draw_callback(self._left_wall, self._colors["wall"])
        else:
            self._draw_callback(self._left_wall, self._colors["bg"])

    def draw_move(self, to_cell: "Cell", undo=False) -> None:
        if self._draw_callback is None:
            return

        move_line_color = self._colors["path"]
        if undo:
            move_line_color = self._colors["err"]

        move_line = Line(self._center_point, to_cell._center_point)
        self._draw_callback(move_line, move_line_color)

    def draw_exit(self) -> None:
        if self._draw_callback is None:
            return

        line = Line(self._center_point, self._bottom_wall_midpoint)
        self._draw_callback(line, self._colors["path"])

    def draw_entry(self, undo=False) -> None:
        if self._draw_callback is None:
            return
        move_color = self._colors["path"]
        if undo:
            move_color = self._colors["err"]

        line = Line(self._top_wall_midpoint, self._center_point)
        self._draw_callback(line, move_color)
