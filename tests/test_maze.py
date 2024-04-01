import unittest

from src.models import Cell, Line, Point, Maze


class TestMaze(unittest.TestCase):
    def test_maze_creates_cell_grid(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_creates_cell_grid_2(self):
        num_cols = 50
        num_rows = 2
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_creates_cell_grid_3(self):
        num_cols = 1
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_fails_if_no_size(self):
        num_cols = 0
        num_rows = 0
        with self.assertRaises(IndexError) as e:
            Maze(0, 0, num_rows, num_cols, 10, 10, None)

    def test_maze_creates_cell(self):
        num_cols = 12
        num_rows = 10
        cell_size = 10
        m1 = Maze(0, 0, num_rows, num_cols, cell_size, 10, None)
        cell = m1._cells[0][0]

        self.assertIsInstance(cell, Cell)
        self.assertEqual(cell._top_wall, Line(Point(0, 0), Point(10, 0)))

    def test_breaks_entry_exit_cells(self):
        num_cols = 5
        nums_rows = 2
        cell_size = 10
        maze = Maze(0, 0, nums_rows, num_cols, cell_size, cell_size, None)
        entry_cell = maze._cells[0][0]
        exit_cell = maze._cells[nums_rows - 1][num_cols - 1]

        self.assertIsInstance(entry_cell, Cell)
        self.assertIsInstance(exit_cell, Cell)

        self.assertEqual(entry_cell.has_top_wall, False)

        self.assertEqual(exit_cell.has_bottom_wall, False)
