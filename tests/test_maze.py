import unittest

from src.models import Cell, Line, Point, Maze


class TestMaze(unittest.TestCase):
    def test_maze_creates_cell_grid(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, None)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_creates_cell_grid_2(self):
        num_cols = 50
        num_rows = 2
        m1 = Maze(0, 0, num_rows, num_cols, 10, None)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_creates_cell_grid_3(self):
        num_cols = 1
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, None)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_creates_cell_grid_4(self):
        num_cols = 0
        num_rows = 0
        m1 = Maze(0, 0, num_rows, num_cols, 10, None)
        self.assertEqual(m1._cells, [])

    def test_maze_creates_cell(self):
        num_cols = 12
        num_rows = 10
        cell_size = 10
        m1 = Maze(0, 0, num_rows, num_cols, cell_size, None)
        cell = m1._cells[0][0]

        self.assertIsInstance(cell, Cell)
        self.assertEqual(cell._top_wall, Line(Point(0, 0), Point(10, 0)))
