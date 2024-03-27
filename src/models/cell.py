from . import Line, Window, Point


class Cell:
    def __init__(
        self,
        window: Window,
        x: int,
        y: int,
        size: int,
        has_top_wall: bool = True,
        has_right_wall: bool = True,
        has_bottom_wall: bool = True,
        has_left_wall: bool = True,
    ) -> None:
        top_left = Point(x, y)
        top_right = Point(x + size, y)
        bottom_left = Point(x, y + size)
        bottom_right = Point(x + size, y + size)
        center = Point(x + size // 2, y + size // 2)

        self.__wall_color = "green2"
        self.__window = window
        self.__center_point = center
        self.__top_wall = Line(top_left, top_right)
        self.__right_wall = Line(top_right, bottom_right)
        self.__bottom_wall = Line(bottom_left, bottom_right)
        self.__left_wall = Line(top_left, bottom_left)
        self.has_top_wall = has_top_wall
        self.has_right_wall = has_right_wall
        self.has_bottom_wall = has_bottom_wall
        self.has_left_wall = has_left_wall

    def draw(self) -> None:
        if self.has_top_wall:
            self.__window.draw_line(self.__top_wall, self.__wall_color)

        if self.has_right_wall:
            self.__window.draw_line(self.__right_wall, self.__wall_color)

        if self.has_bottom_wall:
            self.__window.draw_line(self.__bottom_wall, self.__wall_color)

        if self.has_left_wall:
            self.__window.draw_line(self.__left_wall, self.__wall_color)

    def draw_move(self, to_cell: "Cell", undo=False) -> None:
        move_line_color = self.__wall_color
        if undo:
            move_line_color = "red"

        move_line = Line(self.__center_point, to_cell.__center_point)
        self.__window.draw_line(move_line, move_line_color)