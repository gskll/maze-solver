import time
import random
from cell import Cell
from window import Window


class Maze:
    def __init__(
        self,
        x: int,
        y: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        window: Window | None = None,
        seed: int | None = None,
    ) -> None:
        if seed is not None:
            random.seed(seed)

        self._cells: list[list[Cell]] = []
        self._window = window
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_visited_cells()

    def _create_cells(self):
        for r in range(self._num_rows):
            y = self._y + r * self._cell_size_y
            row = []
            for c in range(self._num_cols):
                x = self._x + c * self._cell_size_x
                cell = Cell(
                    x, y, self._cell_size_x, self._cell_size_y, window=self._window
                )
                row.append(cell)
            self._cells.append(row)

        for row in self._cells:
            for cell in row:
                self._draw_cell(cell)

    def _draw_cell(self, cell: Cell):
        cell.draw()
        self._animate()

    def _animate(self):
        if self._window is None:
            return
        self._window.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        entry_cell = self._cells[0][0]
        exit_cell = self._cells[self._num_rows - 1][self._num_cols - 1]

        entry_cell.has_top_wall = False
        exit_cell.has_bottom_wall = False
        self._draw_cell(entry_cell)
        self._draw_cell(exit_cell)

    def _break_walls_r(self, row: int, col: int):
        cell = self._cells[row][col]
        cell.visited = True

        while True:
            possible_next_moves = self._find_possible_next_moves(row, col)
            if len(possible_next_moves) == 0:
                self._draw_cell(cell)
                return

            next_index = random.randrange(len(possible_next_moves))
            next_move = possible_next_moves[next_index]
            next_row, next_col = next_move[0], next_move[1]
            next_cell = self._cells[next_row][next_col]

            # above
            if next_row == row - 1:
                cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            # left
            if next_col == col - 1:
                cell.has_left_wall = False
                next_cell.has_right_wall = False
            # below
            if next_row == row + 1:
                cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            # right
            if next_col == col + 1:
                cell.has_right_wall = False
                next_cell.has_left_wall = False

            self._break_walls_r(next_row, next_col)

    def _find_possible_next_moves(self, row: int, col: int) -> list[tuple[int, int]]:
        moves = []

        # above
        if row > 0:
            moves.append((row - 1, col))
        # left
        if col > 0:
            moves.append((row, col - 1))
        # below
        if row < self._num_rows - 1:
            moves.append((row + 1, col))
        # right
        if col < self._num_cols - 1:
            moves.append((row, col + 1))

        return [move for move in moves if not self._cells[move[0]][move[1]].visited]

    def _reset_visited_cells(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False
