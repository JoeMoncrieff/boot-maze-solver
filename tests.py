import unittest

from maze import Maze
from drawing import Cell

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_rows,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_cols,
        )
        self.assertEqual(
            m1.cells[0][0],
            Cell(0,0,10,10,window=None)
        )


        num_rows = 20
        num_cols = 50
        m2 = Maze(0,0,num_rows,num_cols, 11,12)
        self.assertEqual(
            num_rows,
            len(m2.cells)
        )
        self.assertEqual(
            num_cols,
            len(m2.cells[0])
        )

if __name__ == "__main__":
    unittest.main()