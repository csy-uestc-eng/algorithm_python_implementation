from unittest import TestCase
from number_of_islands import Solution


class TestSolution(TestCase):
    def test_numIslands(self):
        Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
