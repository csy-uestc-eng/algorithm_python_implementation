from unittest import TestCase
from maze_307 import Maze, Node, input_handle


class TestMaze(TestCase):

    def test_get_min_path(self):
        array = [
            ['1', '0', '1'],
            ['0', 'S', '1'],
            ['0', '0', 'E']
        ]
        maze = Maze(3, 3, array)
        cnt = maze.shortest_path((1, 1))
        self.assertEqual(cnt, 2)

    def test_get_min_path01(self):
        array = [
            ['S', '1', 'E']]
        maze = Maze(1, 3, array)
        cnt = maze.shortest_path((0, 0))
        self.assertEqual(cnt, 'no way')

    def test_get_min_path02(self):
        array = [
            ['S', '0', '0']]
        maze = Maze(1, 3, array)
        cnt = maze.shortest_path((0, 0))
        self.assertEqual(cnt, 'no way')



