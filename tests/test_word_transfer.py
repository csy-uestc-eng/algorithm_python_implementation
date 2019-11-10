from unittest import TestCase
from word_transfer import Solution, Solution02

class TestSolution(TestCase):
    def test_ladderLength(self):
        print(Solution().ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))

    def test_solution02(self):
        print(Solution02().findLadders('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
