import time
from tkinter import TOP, X, Frame, Tk, BOTH, Canvas

from button import Btn
from line import Line
from maze import Maze


def lock(func):
    def wrapper(self, *args, **kwargs):
        if self._is_working:
            print(f"cannot run {func.__name__} while working")
            return

        self._is_working = True
        try:
            result = func(self, *args, **kwargs)
        except Exception as e:
            raise e
        finally:
            self._is_working = False
        return result

    return wrapper


class Window:
    def __init__(self, height: int, width: int):
        self._is_working = False
        self._running = False
        self._main_color = "green"
        self._bg_color = "gray3"
        self._wall_color = "green2"

        self._root: Tk = Tk()
        self._root.title("Maze Solver")
        self._root.protocol("WM_DELETE_WINDOW", self.close)

        self._canvas: Canvas = Canvas(
            self._root, height=height, width=width, bg=self._bg_color
        )
        self._canvas.pack(fill=BOTH, expand=1)

        self._make_buttons()
        self._setup_maze(height, width)

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

    def animate(self):
        self.redraw()
        time.sleep(0.01)

    @lock
    def _solve_dfs(self):
        print("solving dfs")
        self._maze.solve_dfs()

    @lock
    def _solve_bfs(self):
        print("solving bfs")
        self._maze.solve_bfs()

    @lock
    def _new_path(self):
        print("new maze path")
        self._canvas.delete("all")
        self.redraw()
        self._maze.make_path()

    @lock
    def _setup_maze(self, screen_y, screen_x):
        print("setting up maze")
        margin = 50
        num_rows = 12
        num_cols = 16
        cell_size_x = (screen_x - 2 * margin) // num_cols
        cell_size_y = (screen_y - 2 * margin) // num_rows

        self._maze = Maze(
            margin,
            margin,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            self._wall_color,
            self._bg_color,
            self.draw_line,
            cell_animator=self.animate,
            path_animator=self.animate,
        )
        self._maze.make_path()

    def _make_buttons(self):
        self._button_frame = Frame(self._root, bg=self._bg_color)
        self._button_frame.pack(fill=X, side=TOP, padx=10, pady=10)

        Btn(
            self._button_frame,
            "New Path",
            self._new_path,
            self._main_color,
            self._bg_color,
        )

        Btn(
            self._button_frame,
            "Solve - DFS",
            self._solve_dfs,
            self._main_color,
            self._bg_color,
        )

        Btn(
            self._button_frame,
            "Solve - BFS",
            self._solve_bfs,
            self._main_color,
            self._bg_color,
        )
