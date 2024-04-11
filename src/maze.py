import random
from typing import Callable
from cell import Cell
from line import Line


class Maze:
    def __init__(
        self,
        x: int,
        y: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        wall_color: str,
        bg_color: str,
        draw_callback: Callable[[Line, str], None] | None = None,
        cell_animator: Callable | None = None,
        path_animator: Callable | None = None,
        seed: int | None = None,
    ) -> None:
        if seed is not None:
            random.seed(seed)

        self._cells: list[list[Cell]] = []
        self._draw_callback = draw_callback
        self._cell_animator = cell_animator
        self._path_animator = path_animator
        self._wall_color = wall_color
        self._bg_color = bg_color
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._create_cells()

    def make_path(self):
        self._reset_cell_walls()
        self._reset_visited_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_visited_cells()

    def _create_cells(self):
        cells = []
        for r in range(self._num_rows):
            y = self._y + r * self._cell_size_y
            row = []
            for c in range(self._num_cols):
                x = self._x + c * self._cell_size_x
                cell = Cell(
                    x,
                    y,
                    self._cell_size_x,
                    self._cell_size_y,
                    self._wall_color,
                    self._bg_color,
                    self._draw_callback,
                )
                row.append(cell)
            cells.append(row)

        self._cells = cells

        for row in self._cells:
            for cell in row:
                self._draw_cell(cell)

    def _draw_cell(self, cell: Cell):
        cell.draw()
        if self._cell_animator:
            self._cell_animator()

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

    def _reset_cell_walls(self):
        for row in self._cells:
            for cell in row:
                cell.has_top_wall = True
                cell.has_left_wall = True
                cell.has_right_wall = True
                cell.has_bottom_wall = True

    def _reset_visited_cells(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def _is_entry_cell(self, row: int, col: int) -> bool:
        return row == 0 and col == 0

    def _is_exit_cell(self, row: int, col: int) -> bool:
        return row == self._num_rows - 1 and col == self._num_cols - 1

    def solve_dfs(self) -> bool:
        self._cells[0][0].draw_entry()
        return self._solve_dfs_r(0, 0)

    def _solve_dfs_r(self, row: int, col: int) -> bool:
        if self._path_animator:
            self._path_animator()

        cell = self._cells[row][col]

        if self._is_exit_cell(row, col):
            cell.draw_exit()
            return True

        cell.visited = True

        if not cell.has_top_wall and not self._is_entry_cell(row, col):
            next_cell = self._cells[row - 1][col]
            if next_cell and not next_cell.visited:
                cell.draw_move(next_cell)
                right_move = self._solve_dfs_r(row - 1, col)
                if right_move:
                    return True
                next_cell.draw_move(cell, undo=True)

        if not cell.has_right_wall:
            next_cell = self._cells[row][col + 1]
            if next_cell and not next_cell.visited:
                cell.draw_move(next_cell)
                right_move = self._solve_dfs_r(row, col + 1)
                if right_move:
                    return True
                next_cell.draw_move(cell, undo=True)

        if not cell.has_bottom_wall and not self._is_exit_cell(row, col):
            next_cell = self._cells[row + 1][col]
            if next_cell and not next_cell.visited:
                cell.draw_move(next_cell)
                right_move = self._solve_dfs_r(row + 1, col)
                if right_move:
                    return True
                next_cell.draw_move(cell, undo=True)

        if not cell.has_left_wall:
            next_cell = self._cells[row][col - 1]
            if next_cell and not next_cell.visited:
                cell.draw_move(next_cell)
                right_move = self._solve_dfs_r(row, col - 1)
                if right_move:
                    return True
                next_cell.draw_move(cell, undo=True)

        return False

    def solve_bfs(self) -> bool:
        self._cells[0][0].draw_entry(undo=True)
        to_visit: list[tuple[int, int]] = [(0, 0)]
        came_from: dict[tuple[int, int], tuple[int, int] | None] = {(0, 0): None}

        while len(to_visit) != 0:
            row, col = to_visit.pop(0)
            if self._path_animator:
                self._path_animator()

            cell = self._cells[row][col]
            if self._is_exit_cell(row, col):
                cell.draw_exit()
                self._retrace_path(came_from, row, col)
                return True

            cell.visited = True

            if not cell.has_top_wall and not self._is_entry_cell(row, col):
                next_cell = self._cells[row - 1][col]
                if next_cell and not next_cell.visited:
                    cell.draw_move(next_cell, undo=True)
                    to_visit.append((row - 1, col))
                    came_from[(row - 1, col)] = (row, col)

            if not cell.has_right_wall:
                next_cell = self._cells[row][col + 1]
                if next_cell and not next_cell.visited:
                    cell.draw_move(next_cell, undo=True)
                    to_visit.append((row, col + 1))
                    came_from[(row, col + 1)] = (row, col)

            if not cell.has_bottom_wall and not self._is_exit_cell(row, col):
                next_cell = self._cells[row + 1][col]
                if next_cell and not next_cell.visited:
                    cell.draw_move(next_cell, undo=True)
                    to_visit.append((row + 1, col))
                    came_from[(row + 1, col)] = (row, col)

            if not cell.has_left_wall:
                next_cell = self._cells[row][col - 1]
                if next_cell and not next_cell.visited:
                    cell.draw_move(next_cell, undo=True)
                    to_visit.append((row, col - 1))
                    came_from[(row, col - 1)] = (row, col)

        return False

    def _retrace_path(
        self,
        came_from: dict[tuple[int, int], tuple[int, int] | None],
        row: int,
        col: int,
    ):
        curr = (row, col)

        while curr in came_from:
            curr_cell = self._cells[curr[0]][curr[1]]
            prev = came_from[curr]
            if not prev:
                break
            prev_cell = self._cells[prev[0]][prev[1]]

            curr_cell.draw_move(prev_cell)
            curr = prev

        self._cells[curr[0]][curr[1]].draw_entry()
