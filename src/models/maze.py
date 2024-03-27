import time
from . import Window, Cell


class Maze:
    def __init__(
        self,
        x: int,
        y: int,
        num_rows: int,
        num_cols: int,
        cell_size: int,
        window: Window | None = None,
    ) -> None:
        self._cells: list[list[Cell]] = []
        self._window = window
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size = cell_size
        self._create_cells()

    def _create_cells(self):
        for r in range(self._num_rows):
            y = self._y + r * self._cell_size
            row = []
            for c in range(self._num_cols):
                x = self._x + c * self._cell_size
                cell = Cell(x, y, self._cell_size, window=self._window)
                row.append(cell)
            self._cells.append(row)

        for row in self._cells:
            for cell in row:
                self._draw_cell(cell)

        self._break_entrance_and_exit()

    def _draw_cell(self, cell: Cell):
        cell.draw()
        self._animate()

    def _animate(self):
        if self._window is None:
            return
        self._window.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entry_cell = self._cells[0][0]
        exit_cell = self._cells[self._num_rows - 1][self._num_cols - 1]

        entry_cell.has_top_wall = False
        exit_cell.has_bottom_wall = False
        self._draw_cell(entry_cell)
        self._draw_cell(exit_cell)
