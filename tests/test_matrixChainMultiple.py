from unittest import TestCase
from MatrixChainOrder import MatrixChainMultiple


class TestMatrixChainMultiple(TestCase):

    def test_matrix_multiple(self):
        matrixa = [
            [1, 2],
            [2, 3]
        ]
        matrixb = [
            [1, 2, 3],
            [3, 2, 1]
        ]
        result_matrix = [
            [7, 6, 5],
            [11, 10, 9]
        ]
        matrix_magr = MatrixChainMultiple()
        result = matrix_magr.matrix_multiple(matrixa, matrixb)
        self.assertEqual(True, matrix_magr.matrix_equal(result, result_matrix))

    def test_matrix_order(self):
        matrix_magr = MatrixChainMultiple()
        p = [30, 35, 15, 5, 10, 20, 25]
        cij, sij = matrix_magr.matrix_order(p)
        self.assertEqual('((A0(A1A2))((A3A4)A5))', matrix_magr.get_matrix_order(sij, 0, 5))
        self.assertEqual(cij[0][5], 15125)

    def test_matrix_order01(self):
        matrix_magr = MatrixChainMultiple()
        p = [5, 10, 3, 12, 5, 50, 6]
        cij, sij = matrix_magr.matrix_order(p)
        self.assertEqual('((A0A1)((A2A3)(A4A5)))', matrix_magr.get_matrix_order(sij, 0, 5))
        self.assertEqual(cij[0][5], 2010)

    def test_matrix_mul(self):
        matrix = MatrixChainMultiple()
        result_matrix = [
            [7, 6, 5],
            [11, 10, 9]
        ]
        arrays = [
            [
                [1, 2],
                [2, 3]
            ],
            [
                [1, 2, 3],
                [3, 2, 1]
            ]
        ]
        self.assertEqual(True, matrix.matrix_equal(
            result_matrix, matrix.matrix_mul(arrays)))
