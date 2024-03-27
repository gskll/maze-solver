from . import Line, Window, Point


class Cell:
    def __init__(
        self,
        x: int,
        y: int,
        size: int,
        has_top_wall: bool = True,
        has_right_wall: bool = True,
        has_bottom_wall: bool = True,
        has_left_wall: bool = True,
        window: Window | None = None,
    ) -> None:
        top_left = Point(x, y)
        top_right = Point(x + size, y)
        bottom_left = Point(x, y + size)
        bottom_right = Point(x + size, y + size)
        center = Point(x + size // 2, y + size // 2)

        self._wall_color = "green2"
        self._window = window
        self._center_point = center
        self._top_wall = Line(top_left, top_right)
        self._right_wall = Line(top_right, bottom_right)
        self._bottom_wall = Line(bottom_left, bottom_right)
        self._left_wall = Line(top_left, bottom_left)
        self.has_top_wall = has_top_wall
        self.has_right_wall = has_right_wall
        self.has_bottom_wall = has_bottom_wall
        self.has_left_wall = has_left_wall

    def draw(self) -> None:
        if self._window is None:
            return

        if self.has_top_wall:
            self._window.draw_line(self._top_wall, self._wall_color)
        else:
            self._window.draw_line(self._top_wall, self._window._bg_color)

        if self.has_right_wall:
            self._window.draw_line(self._right_wall, self._wall_color)
        else:
            self._window.draw_line(self._right_wall, self._window._bg_color)

        if self.has_bottom_wall:
            self._window.draw_line(self._bottom_wall, self._wall_color)
        else:
            self._window.draw_line(self._bottom_wall, self._window._bg_color)

        if self.has_left_wall:
            self._window.draw_line(self._left_wall, self._wall_color)
        else:
            self._window.draw_line(self._left_wall, self._window._bg_color)

    def draw_move(self, to_cell: "Cell", undo=False) -> None:
        if self._window is None:
            return

        move_line_color = self._wall_color
        if undo:
            move_line_color = "red"

        move_line = Line(self._center_point, to_cell._center_point)
        self._window.draw_line(move_line, move_line_color)
