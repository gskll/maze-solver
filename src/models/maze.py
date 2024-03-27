import time
from src.models.cell import Cell
from . import Window


class Maze:
    def __init__(
        self,
        window: Window,
        x: int,
        y: int,
        num_rows: int,
        num_cols: int,
        cell_size: int,
    ) -> None:
        self._cells = []
        self._window = window
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size = cell_size
        self._create_cells()

    def _create_cells(self):
        for c in range(self._num_cols):
            y = self._y + c * self._cell_size
            row = []
            for r in range(self._num_rows):
                x = self._x + r * self._cell_size
                cell = Cell(self._window, x, y, self._cell_size)
                row.append(cell)
            self._cells.append(row)

        for row in self._cells:
            for cell in row:
                self._draw_cell(cell)

    def _draw_cell(self, cell: Cell):
        cell.draw()
        self._animate()

    def _animate(self):
        self._window.redraw()
        time.sleep(0.05)
