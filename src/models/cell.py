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

        self.__wall_color = "green2"
        self.__window = window
        self.__top_wall = Line(top_left, top_right)
        self.__right_wall = Line(top_right, bottom_right)
        self.__bottom_wall = Line(bottom_left, bottom_right)
        self.__left_wall = Line(top_left, bottom_left)
        self.top_wall = has_top_wall
        self.right_wall = has_right_wall
        self.bottom_wall = has_bottom_wall
        self.left_wall = has_left_wall

    def draw(self) -> None:
        if self.top_wall:
            self.__window.draw_line(self.__top_wall, self.__wall_color)

        if self.right_wall:
            self.__window.draw_line(self.__right_wall, self.__wall_color)

        if self.bottom_wall:
            self.__window.draw_line(self.__bottom_wall, self.__wall_color)

        if self.left_wall:
            self.__window.draw_line(self.__left_wall, self.__wall_color)
