from unittest import TestCase
from Dijkstra import dijkstra


class TestDijkstra(TestCase):
    def test_dijkstra(self):
        g = {
            '0': {'1': 1, '2': 3},
            '1': {'2': 1},
            '2': {}
        }
        visited = dijkstra(g, '0')
        self.assertEqual(visited, [('0', 0), ('1', 1), ('2', 2)])

    def test_dijkstra01(self):
        g = {
            '0': {'1': 10, '2': 5},
            '1': {'2': 2, '3': 1},
            '2': {'1': 3, '3': 9, '4': 2},
            '3': {'4': 4},
            '4': {'0': 7, '3': 6}
        }
        visited = dijkstra(g, '0')
        self.assertEqual(visited, [('0', 0), ('2', 5), ('4', 7), ('1', 8), ('3', 9)])
