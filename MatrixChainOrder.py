import sys
class MatrixChainMultiple(object):
    def __init__(self, matrixs=None):
        super(MatrixChainMultiple, self).__init__()
        self.matrixs = matrixs if matrixs else []

    def __get_matrix_row_col(self, matrix):
        matrix_a_row = len(matrix)
        if matrix_a_row == 0:
            return 0, 0
        matrix_a_col = len(matrix[0])
        return matrix_a_row, matrix_a_col

    def matrix_equal(self, matrixa, matrixb):
        arow, acol = self.__get_matrix_row_col(matrixa)
        brow, bcol = self.__get_matrix_row_col(matrixb)
        if arow != brow or acol != bcol:
            return False
        for i in range(arow):
            for j in range(acol):
                if matrixa[i][j] != matrixb[i][j]:
                    return False
        return True

    def matrix_multiple(self, matrix_a, matrix_b):
        """ compute the result of matrix_a * matrix_b

        :param matrix_a: example: [[2, 3], [1, 2], [2,3]]
            means matrix of a 3 rows, 2 columns
        :type matrix_a: []
        :param matrix_b:
        :return: result of matrix_a * matrix_b
        :type return: []
        """
        def __compute(matrix_a, row, matrix_b, col):
            result = 0
            for i in range(len(matrix_a[row])):
                result = result + matrix_a[row][i] * matrix_b[i][col]
            return result

        matrix_a_row, matrix_a_col = self.__get_matrix_row_col(matrix_a)
        matrix_b_row, matrix_b_col = self.__get_matrix_row_col(matrix_b)
        if matrix_a_col != matrix_b_row:
            raise ValueError('Invalid Matrix Multiple')
        result_matrix = [[0] * matrix_b_col for i in range(matrix_a_row)]
        for i in range(matrix_a_row):
            for j in range(matrix_b_col):
                result_matrix[i][j] = __compute(matrix_a, i, matrix_b, j)
        return result_matrix

    def multiple_matrix_mul(self, matrix, i, j):
        matrix_ret = None
        if i == j:
            return matrix[i]
        for m in range(i, j):
            matrix_ret = self.matrix_multiple(matrix[m], matrix[m+1])
        return matrix_ret

    def build_matrixs(self):
        pass

    def get_matrix_order(self, sij, i, j):
        sep = sij[i][j]
        if sep == 0:
            order = ''
            for num in range(i, j+1):
                order = 'A%d' % num + order
            return order
        else:
            order = '('
            lorder = self.get_matrix_order(sij, i, sep-1)
            rorder = self.get_matrix_order(sij, sep, j)
            return '(' + lorder + rorder + ')'


    def matrix_order(self, p):
        length = len(p) - 1
        cij = [[0] * length for i in range(length)]
        sij = [[0] * length for i in range(length)]

        for i in range(length-1, -1, -1):
            for j in range(i, length):
                if i == j:
                    cij[i][j] = 0
                else:
                    min_cnt = sys.maxint
                    for k in range(i, j):
                        cnt = cij[i][k] + cij[k+1][j] + p[i] * p[k+1] * p[j+1]
                        if cnt < min_cnt:
                            min_cnt = cnt
                            sij[i][j] = k + 1
                    cij[i][j] = min_cnt
        return cij, sij

    def get_matrix_scal(self, matrixs):
        p = []
        if len(matrixs) == 0:
            return p
        row, col = self.__get_matrix_row_col(matrixs[0])
        p.append(row)
        p.append(col)
        for i in range(1, len(matrixs)):
            _, col = self.__get_matrix_row_col(matrixs[i])
            p.append(col)
        return p

    def matrix_mul(self, matrixs):
        scale = self.get_matrix_scal(matrixs)
        cij, sij = self.matrix_order(scale)
        return self.compute_by_order(matrixs, sij, 0, len(matrixs) - 1)

    def compute_by_order(self, matrixs, sij, i, j):
        if sij[i][j] == 0:
            return self.multiple_matrix_mul(matrixs, i, j)
        else:
            k = sij[i][j]
            lmatrix = self.compute_by_order(matrixs, sij, i, k-1)
            rmatrix = self.compute_by_order(matrixs, sij, k, j)
            return self.matrix_multiple(lmatrix, rmatrix)

